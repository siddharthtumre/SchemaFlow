from __future__ import annotations

import json

from antlr4 import InputStream, CommonTokenStream

from schemaflow.data.cypher_parser.grammar.Cypher5Lexer import Cypher5Lexer
from schemaflow.data.cypher_parser.grammar.Cypher5Parser import Cypher5Parser
from schemaflow.data.cypher_parser.grammar.Cypher5ParserVisitor import Cypher5ParserVisitor


def _clean(text: str) -> str:
    if len(text) >= 2 and text[0] == "`" and text[-1] == "`":
        return text[1:-1]
    return text


class CypherSchemaExtractor(Cypher5ParserVisitor):
    def __init__(self):
        self.nodes: set[str] = set()
        self.node_props: set[tuple[str, str]] = set()
        self.relations: set[tuple[str, str, str]] = set()
        self.relation_props: set[tuple[str, str]] = set()

        self.var_labels: dict[str, set[str]] = {}
        self.var_rel_types: dict[str, set[str]] = {}

    @staticmethod
    def _labels_from_label_expression(ctx) -> set[str]:
        names: set[str] = set()
        if ctx is None:
            return names

        def walk(node) -> None:
            if node is None:
                return
            # Skip dynamic / wildcard labels entirely - nothing static to extract
            if isinstance(
                node,
                (
                    Cypher5Parser.DynamicLabelContext,
                    Cypher5Parser.DynamicLabelIsContext,
                    Cypher5Parser.AnyLabelContext,
                    Cypher5Parser.AnyLabelIsContext,
                ),
            ):
                return
            if isinstance(node, Cypher5Parser.LabelNameContext):
                names.add(_clean(node.symbolicNameString().getText()))
                return
            if isinstance(node, Cypher5Parser.LabelNameIsContext):
                names.add(_clean(node.symbolicLabelNameString().getText()))
                return
            for i in range(node.getChildCount()):
                walk(node.getChild(i))

        walk(ctx)
        return names

    @staticmethod
    def _prop_keys(properties_ctx) -> set[str]:
        if properties_ctx is None:
            return set()
        map_ctx = properties_ctx.map_()
        if map_ctx is None:
            return set()
        return {_clean(pk.getText()) for pk in map_ctx.propertyKeyName()}

    @staticmethod
    def _node_var(ctx) -> str | None:
        var = ctx.variable()
        return _clean(var.getText()) if var is not None else None

    @staticmethod
    def _is_left_arrow(ctx) -> bool:
        return ctx.leftArrow() is not None

    def _resolve_node_labels(self, node_ctx) -> set[str]:
        labels = self._labels_from_label_expression(node_ctx.labelExpression())
        if not labels:
            var = self._node_var(node_ctx)
            if var is not None:
                labels = self.var_labels.get(var, set())
        return labels

    def _resolve_rel_types(self, rel_ctx) -> set[str]:
        rtypes = self._labels_from_label_expression(rel_ctx.labelExpression())
        if not rtypes:
            var = rel_ctx.variable()
            if var is not None:
                rtypes = self.var_rel_types.get(_clean(var.getText()), set())
        return rtypes
    
    @staticmethod
    def _find_descendants(ctx, cls):
        found = []
        def walk(node):
            if isinstance(node, cls):
                found.append(node)
            for i in range(node.getChildCount()):
                walk(node.getChild(i))
        walk(ctx)
        return found
    
    @classmethod
    def _first_variable_name(cls, ctx) -> str | None:
        var_ctxs = cls._find_descendants(ctx, Cypher5Parser.VariableContext)
        return _clean(var_ctxs[0].getText()) if var_ctxs else None
    
    def _bind_loop_variable(self, loop_var_ctx, source_expr_ctx) -> None:
        if loop_var_ctx is None or source_expr_ctx is None:
            return
        vname = _clean(loop_var_ctx.getText())
 
        for func in self._find_descendants(source_expr_ctx, Cypher5Parser.FunctionInvocationContext):
            fname_ctx = func.functionName()
            if fname_ctx is None:
                continue
            fname = _clean(fname_ctx.getText()).lower()
            args = func.functionArgument()
            if len(args) != 1:
                continue
            arg_ctx = args[0]
 
            if fname == "relationships":
                rtypes = set()
                for rc in self._find_descendants(arg_ctx, Cypher5Parser.RelationshipPatternContext):
                    rtypes |= self._resolve_rel_types(rc)
                if not rtypes:
                    arg_var = self._first_variable_name(arg_ctx)
                    if arg_var is not None:
                        rtypes = self.var_rel_types.get(arg_var, set())
                if rtypes:
                    self.var_rel_types.setdefault(vname, set()).update(rtypes)
 
            elif fname == "nodes":
                labels = set()
                for nc in self._find_descendants(arg_ctx, Cypher5Parser.NodePatternContext):
                    labels |= self._resolve_node_labels(nc)
                if not labels:
                    arg_var = self._first_variable_name(arg_ctx)
                    if arg_var is not None:
                        labels = self.var_labels.get(arg_var, set())
                if labels:
                    self.var_labels.setdefault(vname, set()).update(labels)
 
    def visitPattern(self, ctx: Cypher5Parser.PatternContext):
        result = self.visitChildren(ctx)
 
        var = ctx.variable()
        anon = ctx.anonymousPattern()
        if var is not None and anon is not None:
            pname = _clean(var.getText())
            labels: set[str] = set()
            for nc in self._find_descendants(anon, Cypher5Parser.NodePatternContext):
                labels |= self._resolve_node_labels(nc)
            rtypes: set[str] = set()
            for rc in self._find_descendants(anon, Cypher5Parser.RelationshipPatternContext):
                rtypes |= self._resolve_rel_types(rc)
            self.var_labels.setdefault(pname, set()).update(labels)
            self.var_rel_types.setdefault(pname, set()).update(rtypes)
 
        return result

    def visitListComprehension(self, ctx: Cypher5Parser.ListComprehensionContext):
        exprs = ctx.expression()
        in_expr = exprs[0] if exprs else None
        self._bind_loop_variable(ctx.variable(), in_expr)
        return self.visitChildren(ctx)
 
    def visitListItemsPredicate(self, ctx: Cypher5Parser.ListItemsPredicateContext):
        self._bind_loop_variable(ctx.variable(), ctx.inExp)
        return self.visitChildren(ctx)
 
    def visitUnwindClause(self, ctx: Cypher5Parser.UnwindClauseContext):
        self._bind_loop_variable(ctx.variable(), ctx.expression())
        return self.visitChildren(ctx)

    def visitNodePattern(self, ctx: Cypher5Parser.NodePatternContext):
        explicit_labels = self._labels_from_label_expression(ctx.labelExpression())
        var = self._node_var(ctx)

        self.nodes |= explicit_labels
        if var is not None:
            self.var_labels.setdefault(var, set()).update(explicit_labels)

        effective_labels = explicit_labels or (self.var_labels.get(var, set()) if var else set())
        for prop in self._prop_keys(ctx.properties()):
            for label in effective_labels:
                self.node_props.add((label, prop))

        return self.visitChildren(ctx)

    def visitRelationshipPattern(self, ctx: Cypher5Parser.RelationshipPatternContext):
        explicit_types = self._labels_from_label_expression(ctx.labelExpression())
        var = ctx.variable()
        vname = _clean(var.getText()) if var is not None else None

        if vname is not None:
            self.var_rel_types.setdefault(vname, set()).update(explicit_types)

        effective_types = explicit_types or (self.var_rel_types.get(vname, set()) if vname else set())
        for prop in self._prop_keys(ctx.properties()):
            for rt in effective_types:
                self.relation_props.add((rt, prop))

        return self.visitChildren(ctx)
    
    def _build_relations_from_chain(self, node_patterns, rel_patterns) -> None:
        if not node_patterns or len(node_patterns) < 2:
            return
        prev_labels = self._resolve_node_labels(node_patterns[0])
        for i, rel_pat in enumerate(rel_patterns):
            if i + 1 >= len(node_patterns):
                break
            next_node = node_patterns[i + 1]
            next_labels = self._resolve_node_labels(next_node)
            rtypes = self._resolve_rel_types(rel_pat)
            if self._is_left_arrow(rel_pat):
                starts, ends = next_labels, prev_labels
            else:
                starts, ends = prev_labels, next_labels
            for s in starts:
                for rt in rtypes:
                    for e in ends:
                        self.relations.add((s, rt, e))
            prev_labels = next_labels

    def visitPatternElement(self, ctx):
        self._build_relations_from_chain(ctx.nodePattern(), ctx.relationshipPattern())
        return self.visitChildren(ctx)
    
    def visitPathPatternNonEmpty(self, ctx: Cypher5Parser.PathPatternNonEmptyContext):
        self._build_relations_from_chain(ctx.nodePattern(), ctx.relationshipPattern())
        return self.visitChildren(ctx)

    def _attribute_prop_to_var(self, vname: str, prop_name: str) -> None:
        if vname in self.var_labels:
            for label in self.var_labels[vname]:
                self.node_props.add((label, prop_name))
        if vname in self.var_rel_types:
            for rt in self.var_rel_types[vname]:
                self.relation_props.add((rt, prop_name))

    def visitPropertyExpression(self, ctx: Cypher5Parser.PropertyExpressionContext):
        expr1 = ctx.expression1()
        var_ctx = expr1.variable() if expr1 is not None else None

        if var_ctx is not None:
            vname = _clean(var_ctx.getText())
            props = ctx.property_()
            if props:
                prop_name = _clean(props[0].propertyKeyName().getText())
                self._attribute_prop_to_var(vname, prop_name)

        return self.visitChildren(ctx)

    def visitExpression2(self, ctx: Cypher5Parser.Expression2Context):
        expr1 = ctx.expression1()
        var_ctx = expr1.variable() if expr1 is not None else None

        if var_ctx is not None:
            vname = _clean(var_ctx.getText())
            postfixes = ctx.postFix()
            if postfixes and isinstance(postfixes[0], Cypher5Parser.PropertyPostfixContext):
                prop_name = _clean(postfixes[0].property_().propertyKeyName().getText())
                self._attribute_prop_to_var(vname, prop_name)

        return self.visitChildren(ctx)
    
    def visitMapProjection(self, ctx: Cypher5Parser.MapProjectionContext):
        var = ctx.variable()
        vname = _clean(var.getText()) if var is not None else None
        if vname is not None:
            for el in ctx.mapProjectionElement():
                pk = el.propertyKeyName()
                prop_ctx = el.property_()
                if pk is not None:
                    self._attribute_prop_to_var(vname, _clean(pk.getText()))
                elif prop_ctx is not None:
                    prop_name = _clean(prop_ctx.propertyKeyName().getText())
                    self._attribute_prop_to_var(vname, prop_name)
        return self.visitChildren(ctx)

    def visitSetLabels(self, ctx: Cypher5Parser.SetLabelsContext):
        vname = _clean(ctx.variable().getText())
        labels = {_clean(lt.symbolicNameString().getText()) for lt in ctx.nodeLabels().labelType()}

        self.nodes |= labels
        self.var_labels.setdefault(vname, set()).update(labels)

        return self.visitChildren(ctx)

    def visitSetLabelsIs(self, ctx: Cypher5Parser.SetLabelsIsContext):
        vname = _clean(ctx.variable().getText())
        nl_is = ctx.nodeLabelsIs()

        labels: set[str] = set()
        sym = nl_is.symbolicNameString()
        if sym is not None:
            labels.add(_clean(sym.getText()))
        labels |= {_clean(lt.symbolicNameString().getText()) for lt in nl_is.labelType()}

        self.nodes |= labels
        self.var_labels.setdefault(vname, set()).update(labels)

        return self.visitChildren(ctx)


    def extract(self, tree) -> dict:
        self.visit(tree)
        return {
            "nodes": self.nodes,
            "node_props": self.node_props,
            "relations": self.relations,
            "relation_props": self.relation_props,
        }


def extract_schema(cypher_query: str) -> dict:
    input_stream = InputStream(cypher_query)
    lexer = Cypher5Lexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = Cypher5Parser(tokens)
    tree = parser.statements()
    # print("=" * 80)
    # print(f"Parse tree: {tree.toStringTree(recog=parser)}")
    # print("=" * 80)
    return CypherSchemaExtractor().extract(tree)


if __name__ == "__main__":
    query = """
        MATCH (a:Person)-[r:KNOWS]->(b:Person) 
        WHERE ALL(x IN relationships((a)-[r:KNOWS]->(b)) WHERE x.since > 2020)
        RETURN a
    """
    result = extract_schema(query)

    out = {k: sorted(v) for k, v in result.items()}
    print(json.dumps(out, indent=2, default=list))