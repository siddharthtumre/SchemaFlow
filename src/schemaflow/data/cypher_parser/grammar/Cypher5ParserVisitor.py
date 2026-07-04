# Generated from grammar/Cypher5Parser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .Cypher5Parser import Cypher5Parser
else:
    from Cypher5Parser import Cypher5Parser

# This class defines a complete generic visitor for a parse tree produced by Cypher5Parser.

class Cypher5ParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by Cypher5Parser#statements.
    def visitStatements(self, ctx:Cypher5Parser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#statement.
    def visitStatement(self, ctx:Cypher5Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#periodicCommitQueryHintFailure.
    def visitPeriodicCommitQueryHintFailure(self, ctx:Cypher5Parser.PeriodicCommitQueryHintFailureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#regularQuery.
    def visitRegularQuery(self, ctx:Cypher5Parser.RegularQueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#singleQuery.
    def visitSingleQuery(self, ctx:Cypher5Parser.SingleQueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#clause.
    def visitClause(self, ctx:Cypher5Parser.ClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#useClause.
    def visitUseClause(self, ctx:Cypher5Parser.UseClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#graphReference.
    def visitGraphReference(self, ctx:Cypher5Parser.GraphReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#finishClause.
    def visitFinishClause(self, ctx:Cypher5Parser.FinishClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#returnClause.
    def visitReturnClause(self, ctx:Cypher5Parser.ReturnClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#returnBody.
    def visitReturnBody(self, ctx:Cypher5Parser.ReturnBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#returnItem.
    def visitReturnItem(self, ctx:Cypher5Parser.ReturnItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#returnItems.
    def visitReturnItems(self, ctx:Cypher5Parser.ReturnItemsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#orderItem.
    def visitOrderItem(self, ctx:Cypher5Parser.OrderItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#ascToken.
    def visitAscToken(self, ctx:Cypher5Parser.AscTokenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#descToken.
    def visitDescToken(self, ctx:Cypher5Parser.DescTokenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#orderBy.
    def visitOrderBy(self, ctx:Cypher5Parser.OrderByContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#skip.
    def visitSkip(self, ctx:Cypher5Parser.SkipContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#limit.
    def visitLimit(self, ctx:Cypher5Parser.LimitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#whereClause.
    def visitWhereClause(self, ctx:Cypher5Parser.WhereClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#withClause.
    def visitWithClause(self, ctx:Cypher5Parser.WithClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#createClause.
    def visitCreateClause(self, ctx:Cypher5Parser.CreateClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#insertClause.
    def visitInsertClause(self, ctx:Cypher5Parser.InsertClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#setClause.
    def visitSetClause(self, ctx:Cypher5Parser.SetClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#SetProp.
    def visitSetProp(self, ctx:Cypher5Parser.SetPropContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#SetDynamicProp.
    def visitSetDynamicProp(self, ctx:Cypher5Parser.SetDynamicPropContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#SetProps.
    def visitSetProps(self, ctx:Cypher5Parser.SetPropsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#AddProp.
    def visitAddProp(self, ctx:Cypher5Parser.AddPropContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#SetLabels.
    def visitSetLabels(self, ctx:Cypher5Parser.SetLabelsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#SetLabelsIs.
    def visitSetLabelsIs(self, ctx:Cypher5Parser.SetLabelsIsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#removeClause.
    def visitRemoveClause(self, ctx:Cypher5Parser.RemoveClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#RemoveProp.
    def visitRemoveProp(self, ctx:Cypher5Parser.RemovePropContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#RemoveDynamicProp.
    def visitRemoveDynamicProp(self, ctx:Cypher5Parser.RemoveDynamicPropContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#RemoveLabels.
    def visitRemoveLabels(self, ctx:Cypher5Parser.RemoveLabelsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#RemoveLabelsIs.
    def visitRemoveLabelsIs(self, ctx:Cypher5Parser.RemoveLabelsIsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#deleteClause.
    def visitDeleteClause(self, ctx:Cypher5Parser.DeleteClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#matchClause.
    def visitMatchClause(self, ctx:Cypher5Parser.MatchClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#matchMode.
    def visitMatchMode(self, ctx:Cypher5Parser.MatchModeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#hint.
    def visitHint(self, ctx:Cypher5Parser.HintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#expandHintStep.
    def visitExpandHintStep(self, ctx:Cypher5Parser.ExpandHintStepContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#mergeClause.
    def visitMergeClause(self, ctx:Cypher5Parser.MergeClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#mergeAction.
    def visitMergeAction(self, ctx:Cypher5Parser.MergeActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#unwindClause.
    def visitUnwindClause(self, ctx:Cypher5Parser.UnwindClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#callClause.
    def visitCallClause(self, ctx:Cypher5Parser.CallClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#procedureName.
    def visitProcedureName(self, ctx:Cypher5Parser.ProcedureNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#procedureArgument.
    def visitProcedureArgument(self, ctx:Cypher5Parser.ProcedureArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#procedureResultItem.
    def visitProcedureResultItem(self, ctx:Cypher5Parser.ProcedureResultItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#loadCSVClause.
    def visitLoadCSVClause(self, ctx:Cypher5Parser.LoadCSVClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#foreachClause.
    def visitForeachClause(self, ctx:Cypher5Parser.ForeachClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#subqueryClause.
    def visitSubqueryClause(self, ctx:Cypher5Parser.SubqueryClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#subqueryScope.
    def visitSubqueryScope(self, ctx:Cypher5Parser.SubqueryScopeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#subqueryInTransactionsParameters.
    def visitSubqueryInTransactionsParameters(self, ctx:Cypher5Parser.SubqueryInTransactionsParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#subqueryInTransactionsBatchParameters.
    def visitSubqueryInTransactionsBatchParameters(self, ctx:Cypher5Parser.SubqueryInTransactionsBatchParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#subqueryInTransactionsErrorParameters.
    def visitSubqueryInTransactionsErrorParameters(self, ctx:Cypher5Parser.SubqueryInTransactionsErrorParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#subqueryInTransactionsRetryParameters.
    def visitSubqueryInTransactionsRetryParameters(self, ctx:Cypher5Parser.SubqueryInTransactionsRetryParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#subqueryInTransactionsReportParameters.
    def visitSubqueryInTransactionsReportParameters(self, ctx:Cypher5Parser.SubqueryInTransactionsReportParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#orderBySkipLimitClause.
    def visitOrderBySkipLimitClause(self, ctx:Cypher5Parser.OrderBySkipLimitClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#patternList.
    def visitPatternList(self, ctx:Cypher5Parser.PatternListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#insertPatternList.
    def visitInsertPatternList(self, ctx:Cypher5Parser.InsertPatternListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#pattern.
    def visitPattern(self, ctx:Cypher5Parser.PatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#insertPattern.
    def visitInsertPattern(self, ctx:Cypher5Parser.InsertPatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#quantifier.
    def visitQuantifier(self, ctx:Cypher5Parser.QuantifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#anonymousPattern.
    def visitAnonymousPattern(self, ctx:Cypher5Parser.AnonymousPatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#shortestPathPattern.
    def visitShortestPathPattern(self, ctx:Cypher5Parser.ShortestPathPatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#patternElement.
    def visitPatternElement(self, ctx:Cypher5Parser.PatternElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#AnyShortestPath.
    def visitAnyShortestPath(self, ctx:Cypher5Parser.AnyShortestPathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#AllShortestPath.
    def visitAllShortestPath(self, ctx:Cypher5Parser.AllShortestPathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#AnyPath.
    def visitAnyPath(self, ctx:Cypher5Parser.AnyPathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#AllPath.
    def visitAllPath(self, ctx:Cypher5Parser.AllPathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#ShortestGroup.
    def visitShortestGroup(self, ctx:Cypher5Parser.ShortestGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#groupToken.
    def visitGroupToken(self, ctx:Cypher5Parser.GroupTokenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#pathToken.
    def visitPathToken(self, ctx:Cypher5Parser.PathTokenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#pathPatternNonEmpty.
    def visitPathPatternNonEmpty(self, ctx:Cypher5Parser.PathPatternNonEmptyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#nodePattern.
    def visitNodePattern(self, ctx:Cypher5Parser.NodePatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#insertNodePattern.
    def visitInsertNodePattern(self, ctx:Cypher5Parser.InsertNodePatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#parenthesizedPath.
    def visitParenthesizedPath(self, ctx:Cypher5Parser.ParenthesizedPathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#nodeLabels.
    def visitNodeLabels(self, ctx:Cypher5Parser.NodeLabelsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#nodeLabelsIs.
    def visitNodeLabelsIs(self, ctx:Cypher5Parser.NodeLabelsIsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#dynamicExpression.
    def visitDynamicExpression(self, ctx:Cypher5Parser.DynamicExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#dynamicAnyAllExpression.
    def visitDynamicAnyAllExpression(self, ctx:Cypher5Parser.DynamicAnyAllExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#dynamicLabelType.
    def visitDynamicLabelType(self, ctx:Cypher5Parser.DynamicLabelTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#labelType.
    def visitLabelType(self, ctx:Cypher5Parser.LabelTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#relType.
    def visitRelType(self, ctx:Cypher5Parser.RelTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#labelOrRelType.
    def visitLabelOrRelType(self, ctx:Cypher5Parser.LabelOrRelTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#properties.
    def visitProperties(self, ctx:Cypher5Parser.PropertiesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#relationshipPattern.
    def visitRelationshipPattern(self, ctx:Cypher5Parser.RelationshipPatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#insertRelationshipPattern.
    def visitInsertRelationshipPattern(self, ctx:Cypher5Parser.InsertRelationshipPatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#leftArrow.
    def visitLeftArrow(self, ctx:Cypher5Parser.LeftArrowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#arrowLine.
    def visitArrowLine(self, ctx:Cypher5Parser.ArrowLineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#rightArrow.
    def visitRightArrow(self, ctx:Cypher5Parser.RightArrowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#pathLength.
    def visitPathLength(self, ctx:Cypher5Parser.PathLengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#labelExpression.
    def visitLabelExpression(self, ctx:Cypher5Parser.LabelExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#labelExpression4.
    def visitLabelExpression4(self, ctx:Cypher5Parser.LabelExpression4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#labelExpression4Is.
    def visitLabelExpression4Is(self, ctx:Cypher5Parser.LabelExpression4IsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#labelExpression3.
    def visitLabelExpression3(self, ctx:Cypher5Parser.LabelExpression3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#labelExpression3Is.
    def visitLabelExpression3Is(self, ctx:Cypher5Parser.LabelExpression3IsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#labelExpression2.
    def visitLabelExpression2(self, ctx:Cypher5Parser.LabelExpression2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#labelExpression2Is.
    def visitLabelExpression2Is(self, ctx:Cypher5Parser.LabelExpression2IsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#ParenthesizedLabelExpression.
    def visitParenthesizedLabelExpression(self, ctx:Cypher5Parser.ParenthesizedLabelExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#AnyLabel.
    def visitAnyLabel(self, ctx:Cypher5Parser.AnyLabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#DynamicLabel.
    def visitDynamicLabel(self, ctx:Cypher5Parser.DynamicLabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#LabelName.
    def visitLabelName(self, ctx:Cypher5Parser.LabelNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#ParenthesizedLabelExpressionIs.
    def visitParenthesizedLabelExpressionIs(self, ctx:Cypher5Parser.ParenthesizedLabelExpressionIsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#AnyLabelIs.
    def visitAnyLabelIs(self, ctx:Cypher5Parser.AnyLabelIsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#DynamicLabelIs.
    def visitDynamicLabelIs(self, ctx:Cypher5Parser.DynamicLabelIsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#LabelNameIs.
    def visitLabelNameIs(self, ctx:Cypher5Parser.LabelNameIsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#insertNodeLabelExpression.
    def visitInsertNodeLabelExpression(self, ctx:Cypher5Parser.InsertNodeLabelExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#insertRelationshipLabelExpression.
    def visitInsertRelationshipLabelExpression(self, ctx:Cypher5Parser.InsertRelationshipLabelExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#expression.
    def visitExpression(self, ctx:Cypher5Parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#expression11.
    def visitExpression11(self, ctx:Cypher5Parser.Expression11Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#expression10.
    def visitExpression10(self, ctx:Cypher5Parser.Expression10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#expression9.
    def visitExpression9(self, ctx:Cypher5Parser.Expression9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#expression8.
    def visitExpression8(self, ctx:Cypher5Parser.Expression8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#expression7.
    def visitExpression7(self, ctx:Cypher5Parser.Expression7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#StringAndListComparison.
    def visitStringAndListComparison(self, ctx:Cypher5Parser.StringAndListComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#NullComparison.
    def visitNullComparison(self, ctx:Cypher5Parser.NullComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#TypeComparison.
    def visitTypeComparison(self, ctx:Cypher5Parser.TypeComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#NormalFormComparison.
    def visitNormalFormComparison(self, ctx:Cypher5Parser.NormalFormComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#normalForm.
    def visitNormalForm(self, ctx:Cypher5Parser.NormalFormContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#expression6.
    def visitExpression6(self, ctx:Cypher5Parser.Expression6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#expression5.
    def visitExpression5(self, ctx:Cypher5Parser.Expression5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#expression4.
    def visitExpression4(self, ctx:Cypher5Parser.Expression4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#expression3.
    def visitExpression3(self, ctx:Cypher5Parser.Expression3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#expression2.
    def visitExpression2(self, ctx:Cypher5Parser.Expression2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#PropertyPostfix.
    def visitPropertyPostfix(self, ctx:Cypher5Parser.PropertyPostfixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#LabelPostfix.
    def visitLabelPostfix(self, ctx:Cypher5Parser.LabelPostfixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#IndexPostfix.
    def visitIndexPostfix(self, ctx:Cypher5Parser.IndexPostfixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#RangePostfix.
    def visitRangePostfix(self, ctx:Cypher5Parser.RangePostfixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#property.
    def visitProperty(self, ctx:Cypher5Parser.PropertyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#dynamicProperty.
    def visitDynamicProperty(self, ctx:Cypher5Parser.DynamicPropertyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#propertyExpression.
    def visitPropertyExpression(self, ctx:Cypher5Parser.PropertyExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#dynamicPropertyExpression.
    def visitDynamicPropertyExpression(self, ctx:Cypher5Parser.DynamicPropertyExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#expression1.
    def visitExpression1(self, ctx:Cypher5Parser.Expression1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#NumericLiteral.
    def visitNumericLiteral(self, ctx:Cypher5Parser.NumericLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#StringsLiteral.
    def visitStringsLiteral(self, ctx:Cypher5Parser.StringsLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#OtherLiteral.
    def visitOtherLiteral(self, ctx:Cypher5Parser.OtherLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#BooleanLiteral.
    def visitBooleanLiteral(self, ctx:Cypher5Parser.BooleanLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#KeywordLiteral.
    def visitKeywordLiteral(self, ctx:Cypher5Parser.KeywordLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#caseExpression.
    def visitCaseExpression(self, ctx:Cypher5Parser.CaseExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#caseAlternative.
    def visitCaseAlternative(self, ctx:Cypher5Parser.CaseAlternativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#extendedCaseExpression.
    def visitExtendedCaseExpression(self, ctx:Cypher5Parser.ExtendedCaseExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#extendedCaseAlternative.
    def visitExtendedCaseAlternative(self, ctx:Cypher5Parser.ExtendedCaseAlternativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#WhenStringOrList.
    def visitWhenStringOrList(self, ctx:Cypher5Parser.WhenStringOrListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#WhenNull.
    def visitWhenNull(self, ctx:Cypher5Parser.WhenNullContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#WhenType.
    def visitWhenType(self, ctx:Cypher5Parser.WhenTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#WhenForm.
    def visitWhenForm(self, ctx:Cypher5Parser.WhenFormContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#WhenComparator.
    def visitWhenComparator(self, ctx:Cypher5Parser.WhenComparatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#WhenEquals.
    def visitWhenEquals(self, ctx:Cypher5Parser.WhenEqualsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#listComprehension.
    def visitListComprehension(self, ctx:Cypher5Parser.ListComprehensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#patternComprehension.
    def visitPatternComprehension(self, ctx:Cypher5Parser.PatternComprehensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#reduceExpression.
    def visitReduceExpression(self, ctx:Cypher5Parser.ReduceExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#listItemsPredicate.
    def visitListItemsPredicate(self, ctx:Cypher5Parser.ListItemsPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#normalizeFunction.
    def visitNormalizeFunction(self, ctx:Cypher5Parser.NormalizeFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#trimFunction.
    def visitTrimFunction(self, ctx:Cypher5Parser.TrimFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#patternExpression.
    def visitPatternExpression(self, ctx:Cypher5Parser.PatternExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#shortestPathExpression.
    def visitShortestPathExpression(self, ctx:Cypher5Parser.ShortestPathExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#parenthesizedExpression.
    def visitParenthesizedExpression(self, ctx:Cypher5Parser.ParenthesizedExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#mapProjection.
    def visitMapProjection(self, ctx:Cypher5Parser.MapProjectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#mapProjectionElement.
    def visitMapProjectionElement(self, ctx:Cypher5Parser.MapProjectionElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#countStar.
    def visitCountStar(self, ctx:Cypher5Parser.CountStarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#existsExpression.
    def visitExistsExpression(self, ctx:Cypher5Parser.ExistsExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#countExpression.
    def visitCountExpression(self, ctx:Cypher5Parser.CountExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#collectExpression.
    def visitCollectExpression(self, ctx:Cypher5Parser.CollectExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#numberLiteral.
    def visitNumberLiteral(self, ctx:Cypher5Parser.NumberLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#signedIntegerLiteral.
    def visitSignedIntegerLiteral(self, ctx:Cypher5Parser.SignedIntegerLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#listLiteral.
    def visitListLiteral(self, ctx:Cypher5Parser.ListLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#propertyKeyName.
    def visitPropertyKeyName(self, ctx:Cypher5Parser.PropertyKeyNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#parameter.
    def visitParameter(self, ctx:Cypher5Parser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#parameterName.
    def visitParameterName(self, ctx:Cypher5Parser.ParameterNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#functionInvocation.
    def visitFunctionInvocation(self, ctx:Cypher5Parser.FunctionInvocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#functionArgument.
    def visitFunctionArgument(self, ctx:Cypher5Parser.FunctionArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#functionName.
    def visitFunctionName(self, ctx:Cypher5Parser.FunctionNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#namespace.
    def visitNamespace(self, ctx:Cypher5Parser.NamespaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#variable.
    def visitVariable(self, ctx:Cypher5Parser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#obfuscatedLiteral.
    def visitObfuscatedLiteral(self, ctx:Cypher5Parser.ObfuscatedLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#nonEmptyNameList.
    def visitNonEmptyNameList(self, ctx:Cypher5Parser.NonEmptyNameListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#type.
    def visitType(self, ctx:Cypher5Parser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#typePart.
    def visitTypePart(self, ctx:Cypher5Parser.TypePartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#typeName.
    def visitTypeName(self, ctx:Cypher5Parser.TypeNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#typeNullability.
    def visitTypeNullability(self, ctx:Cypher5Parser.TypeNullabilityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#typeListSuffix.
    def visitTypeListSuffix(self, ctx:Cypher5Parser.TypeListSuffixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#command.
    def visitCommand(self, ctx:Cypher5Parser.CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#createCommand.
    def visitCreateCommand(self, ctx:Cypher5Parser.CreateCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#dropCommand.
    def visitDropCommand(self, ctx:Cypher5Parser.DropCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#showCommand.
    def visitShowCommand(self, ctx:Cypher5Parser.ShowCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#showCommandYield.
    def visitShowCommandYield(self, ctx:Cypher5Parser.ShowCommandYieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#yieldItem.
    def visitYieldItem(self, ctx:Cypher5Parser.YieldItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#yieldSkip.
    def visitYieldSkip(self, ctx:Cypher5Parser.YieldSkipContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#yieldLimit.
    def visitYieldLimit(self, ctx:Cypher5Parser.YieldLimitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#yieldClause.
    def visitYieldClause(self, ctx:Cypher5Parser.YieldClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#commandOptions.
    def visitCommandOptions(self, ctx:Cypher5Parser.CommandOptionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#terminateCommand.
    def visitTerminateCommand(self, ctx:Cypher5Parser.TerminateCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#composableCommandClauses.
    def visitComposableCommandClauses(self, ctx:Cypher5Parser.ComposableCommandClausesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#composableShowCommandClauses.
    def visitComposableShowCommandClauses(self, ctx:Cypher5Parser.ComposableShowCommandClausesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#showBriefAndYield.
    def visitShowBriefAndYield(self, ctx:Cypher5Parser.ShowBriefAndYieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#showIndexCommand.
    def visitShowIndexCommand(self, ctx:Cypher5Parser.ShowIndexCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#showIndexesAllowBrief.
    def visitShowIndexesAllowBrief(self, ctx:Cypher5Parser.ShowIndexesAllowBriefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#showIndexesNoBrief.
    def visitShowIndexesNoBrief(self, ctx:Cypher5Parser.ShowIndexesNoBriefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#ShowConstraintMulti.
    def visitShowConstraintMulti(self, ctx:Cypher5Parser.ShowConstraintMultiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#ShowConstraintUnique.
    def visitShowConstraintUnique(self, ctx:Cypher5Parser.ShowConstraintUniqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#ShowConstraintKey.
    def visitShowConstraintKey(self, ctx:Cypher5Parser.ShowConstraintKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#ShowConstraintRelExist.
    def visitShowConstraintRelExist(self, ctx:Cypher5Parser.ShowConstraintRelExistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#ShowConstraintOldExists.
    def visitShowConstraintOldExists(self, ctx:Cypher5Parser.ShowConstraintOldExistsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#ShowConstraintBriefAndYield.
    def visitShowConstraintBriefAndYield(self, ctx:Cypher5Parser.ShowConstraintBriefAndYieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#constraintAllowYieldType.
    def visitConstraintAllowYieldType(self, ctx:Cypher5Parser.ConstraintAllowYieldTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#constraintExistType.
    def visitConstraintExistType(self, ctx:Cypher5Parser.ConstraintExistTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#constraintBriefAndYieldType.
    def visitConstraintBriefAndYieldType(self, ctx:Cypher5Parser.ConstraintBriefAndYieldTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#showConstraintsAllowBriefAndYield.
    def visitShowConstraintsAllowBriefAndYield(self, ctx:Cypher5Parser.ShowConstraintsAllowBriefAndYieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#showConstraintsAllowBrief.
    def visitShowConstraintsAllowBrief(self, ctx:Cypher5Parser.ShowConstraintsAllowBriefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#showConstraintsAllowYield.
    def visitShowConstraintsAllowYield(self, ctx:Cypher5Parser.ShowConstraintsAllowYieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#showProcedures.
    def visitShowProcedures(self, ctx:Cypher5Parser.ShowProceduresContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#showFunctions.
    def visitShowFunctions(self, ctx:Cypher5Parser.ShowFunctionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#functionToken.
    def visitFunctionToken(self, ctx:Cypher5Parser.FunctionTokenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#executableBy.
    def visitExecutableBy(self, ctx:Cypher5Parser.ExecutableByContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#showFunctionsType.
    def visitShowFunctionsType(self, ctx:Cypher5Parser.ShowFunctionsTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#showTransactions.
    def visitShowTransactions(self, ctx:Cypher5Parser.ShowTransactionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#terminateTransactions.
    def visitTerminateTransactions(self, ctx:Cypher5Parser.TerminateTransactionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#showSettings.
    def visitShowSettings(self, ctx:Cypher5Parser.ShowSettingsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#settingToken.
    def visitSettingToken(self, ctx:Cypher5Parser.SettingTokenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#namesAndClauses.
    def visitNamesAndClauses(self, ctx:Cypher5Parser.NamesAndClausesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#stringsOrExpression.
    def visitStringsOrExpression(self, ctx:Cypher5Parser.StringsOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#commandNodePattern.
    def visitCommandNodePattern(self, ctx:Cypher5Parser.CommandNodePatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#commandRelPattern.
    def visitCommandRelPattern(self, ctx:Cypher5Parser.CommandRelPatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#createConstraint.
    def visitCreateConstraint(self, ctx:Cypher5Parser.CreateConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#ConstraintExists.
    def visitConstraintExists(self, ctx:Cypher5Parser.ConstraintExistsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#ConstraintTyped.
    def visitConstraintTyped(self, ctx:Cypher5Parser.ConstraintTypedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#ConstraintIsUnique.
    def visitConstraintIsUnique(self, ctx:Cypher5Parser.ConstraintIsUniqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#ConstraintKey.
    def visitConstraintKey(self, ctx:Cypher5Parser.ConstraintKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#ConstraintIsNotNull.
    def visitConstraintIsNotNull(self, ctx:Cypher5Parser.ConstraintIsNotNullContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#dropConstraint.
    def visitDropConstraint(self, ctx:Cypher5Parser.DropConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#createIndex.
    def visitCreateIndex(self, ctx:Cypher5Parser.CreateIndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#oldCreateIndex.
    def visitOldCreateIndex(self, ctx:Cypher5Parser.OldCreateIndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#createIndex_.
    def visitCreateIndex_(self, ctx:Cypher5Parser.CreateIndex_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#createFulltextIndex.
    def visitCreateFulltextIndex(self, ctx:Cypher5Parser.CreateFulltextIndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#fulltextNodePattern.
    def visitFulltextNodePattern(self, ctx:Cypher5Parser.FulltextNodePatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#fulltextRelPattern.
    def visitFulltextRelPattern(self, ctx:Cypher5Parser.FulltextRelPatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#createLookupIndex.
    def visitCreateLookupIndex(self, ctx:Cypher5Parser.CreateLookupIndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#lookupIndexNodePattern.
    def visitLookupIndexNodePattern(self, ctx:Cypher5Parser.LookupIndexNodePatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#lookupIndexRelPattern.
    def visitLookupIndexRelPattern(self, ctx:Cypher5Parser.LookupIndexRelPatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#dropIndex.
    def visitDropIndex(self, ctx:Cypher5Parser.DropIndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#propertyList.
    def visitPropertyList(self, ctx:Cypher5Parser.PropertyListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#enclosedPropertyList.
    def visitEnclosedPropertyList(self, ctx:Cypher5Parser.EnclosedPropertyListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#alterCommand.
    def visitAlterCommand(self, ctx:Cypher5Parser.AlterCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#renameCommand.
    def visitRenameCommand(self, ctx:Cypher5Parser.RenameCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#grantCommand.
    def visitGrantCommand(self, ctx:Cypher5Parser.GrantCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#denyCommand.
    def visitDenyCommand(self, ctx:Cypher5Parser.DenyCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#revokeCommand.
    def visitRevokeCommand(self, ctx:Cypher5Parser.RevokeCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#userNames.
    def visitUserNames(self, ctx:Cypher5Parser.UserNamesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#roleNames.
    def visitRoleNames(self, ctx:Cypher5Parser.RoleNamesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#roleToken.
    def visitRoleToken(self, ctx:Cypher5Parser.RoleTokenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#enableServerCommand.
    def visitEnableServerCommand(self, ctx:Cypher5Parser.EnableServerCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#alterServer.
    def visitAlterServer(self, ctx:Cypher5Parser.AlterServerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#renameServer.
    def visitRenameServer(self, ctx:Cypher5Parser.RenameServerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#dropServer.
    def visitDropServer(self, ctx:Cypher5Parser.DropServerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#showServers.
    def visitShowServers(self, ctx:Cypher5Parser.ShowServersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#allocationCommand.
    def visitAllocationCommand(self, ctx:Cypher5Parser.AllocationCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#deallocateDatabaseFromServers.
    def visitDeallocateDatabaseFromServers(self, ctx:Cypher5Parser.DeallocateDatabaseFromServersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#reallocateDatabases.
    def visitReallocateDatabases(self, ctx:Cypher5Parser.ReallocateDatabasesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#createRole.
    def visitCreateRole(self, ctx:Cypher5Parser.CreateRoleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#dropRole.
    def visitDropRole(self, ctx:Cypher5Parser.DropRoleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#renameRole.
    def visitRenameRole(self, ctx:Cypher5Parser.RenameRoleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#showRoles.
    def visitShowRoles(self, ctx:Cypher5Parser.ShowRolesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#grantRole.
    def visitGrantRole(self, ctx:Cypher5Parser.GrantRoleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#revokeRole.
    def visitRevokeRole(self, ctx:Cypher5Parser.RevokeRoleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#createUser.
    def visitCreateUser(self, ctx:Cypher5Parser.CreateUserContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#dropUser.
    def visitDropUser(self, ctx:Cypher5Parser.DropUserContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#renameUser.
    def visitRenameUser(self, ctx:Cypher5Parser.RenameUserContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#alterCurrentUser.
    def visitAlterCurrentUser(self, ctx:Cypher5Parser.AlterCurrentUserContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#alterUser.
    def visitAlterUser(self, ctx:Cypher5Parser.AlterUserContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#removeNamedProvider.
    def visitRemoveNamedProvider(self, ctx:Cypher5Parser.RemoveNamedProviderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#password.
    def visitPassword(self, ctx:Cypher5Parser.PasswordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#passwordOnly.
    def visitPasswordOnly(self, ctx:Cypher5Parser.PasswordOnlyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#passwordExpression.
    def visitPasswordExpression(self, ctx:Cypher5Parser.PasswordExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#passwordChangeRequired.
    def visitPasswordChangeRequired(self, ctx:Cypher5Parser.PasswordChangeRequiredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#userStatus.
    def visitUserStatus(self, ctx:Cypher5Parser.UserStatusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#homeDatabase.
    def visitHomeDatabase(self, ctx:Cypher5Parser.HomeDatabaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#setAuthClause.
    def visitSetAuthClause(self, ctx:Cypher5Parser.SetAuthClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#userAuthAttribute.
    def visitUserAuthAttribute(self, ctx:Cypher5Parser.UserAuthAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#showUsers.
    def visitShowUsers(self, ctx:Cypher5Parser.ShowUsersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#showCurrentUser.
    def visitShowCurrentUser(self, ctx:Cypher5Parser.ShowCurrentUserContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#showSupportedPrivileges.
    def visitShowSupportedPrivileges(self, ctx:Cypher5Parser.ShowSupportedPrivilegesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#showPrivileges.
    def visitShowPrivileges(self, ctx:Cypher5Parser.ShowPrivilegesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#showRolePrivileges.
    def visitShowRolePrivileges(self, ctx:Cypher5Parser.ShowRolePrivilegesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#showUserPrivileges.
    def visitShowUserPrivileges(self, ctx:Cypher5Parser.ShowUserPrivilegesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#privilegeAsCommand.
    def visitPrivilegeAsCommand(self, ctx:Cypher5Parser.PrivilegeAsCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#privilegeToken.
    def visitPrivilegeToken(self, ctx:Cypher5Parser.PrivilegeTokenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#privilege.
    def visitPrivilege(self, ctx:Cypher5Parser.PrivilegeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#allPrivilege.
    def visitAllPrivilege(self, ctx:Cypher5Parser.AllPrivilegeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#allPrivilegeType.
    def visitAllPrivilegeType(self, ctx:Cypher5Parser.AllPrivilegeTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#DefaultTarget.
    def visitDefaultTarget(self, ctx:Cypher5Parser.DefaultTargetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#DatabaseVariableTarget.
    def visitDatabaseVariableTarget(self, ctx:Cypher5Parser.DatabaseVariableTargetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#GraphVariableTarget.
    def visitGraphVariableTarget(self, ctx:Cypher5Parser.GraphVariableTargetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#DBMSTarget.
    def visitDBMSTarget(self, ctx:Cypher5Parser.DBMSTargetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#createPrivilege.
    def visitCreatePrivilege(self, ctx:Cypher5Parser.CreatePrivilegeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#createPrivilegeForDatabase.
    def visitCreatePrivilegeForDatabase(self, ctx:Cypher5Parser.CreatePrivilegeForDatabaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#createNodePrivilegeToken.
    def visitCreateNodePrivilegeToken(self, ctx:Cypher5Parser.CreateNodePrivilegeTokenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#createRelPrivilegeToken.
    def visitCreateRelPrivilegeToken(self, ctx:Cypher5Parser.CreateRelPrivilegeTokenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#createPropertyPrivilegeToken.
    def visitCreatePropertyPrivilegeToken(self, ctx:Cypher5Parser.CreatePropertyPrivilegeTokenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#actionForDBMS.
    def visitActionForDBMS(self, ctx:Cypher5Parser.ActionForDBMSContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#dropPrivilege.
    def visitDropPrivilege(self, ctx:Cypher5Parser.DropPrivilegeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#loadPrivilege.
    def visitLoadPrivilege(self, ctx:Cypher5Parser.LoadPrivilegeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#showPrivilege.
    def visitShowPrivilege(self, ctx:Cypher5Parser.ShowPrivilegeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#setPrivilege.
    def visitSetPrivilege(self, ctx:Cypher5Parser.SetPrivilegeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#passwordToken.
    def visitPasswordToken(self, ctx:Cypher5Parser.PasswordTokenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#removePrivilege.
    def visitRemovePrivilege(self, ctx:Cypher5Parser.RemovePrivilegeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#writePrivilege.
    def visitWritePrivilege(self, ctx:Cypher5Parser.WritePrivilegeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#databasePrivilege.
    def visitDatabasePrivilege(self, ctx:Cypher5Parser.DatabasePrivilegeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#dbmsPrivilege.
    def visitDbmsPrivilege(self, ctx:Cypher5Parser.DbmsPrivilegeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#dbmsPrivilegeExecute.
    def visitDbmsPrivilegeExecute(self, ctx:Cypher5Parser.DbmsPrivilegeExecuteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#adminToken.
    def visitAdminToken(self, ctx:Cypher5Parser.AdminTokenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#procedureToken.
    def visitProcedureToken(self, ctx:Cypher5Parser.ProcedureTokenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#indexToken.
    def visitIndexToken(self, ctx:Cypher5Parser.IndexTokenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#constraintToken.
    def visitConstraintToken(self, ctx:Cypher5Parser.ConstraintTokenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#transactionToken.
    def visitTransactionToken(self, ctx:Cypher5Parser.TransactionTokenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#userQualifier.
    def visitUserQualifier(self, ctx:Cypher5Parser.UserQualifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#executeFunctionQualifier.
    def visitExecuteFunctionQualifier(self, ctx:Cypher5Parser.ExecuteFunctionQualifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#executeProcedureQualifier.
    def visitExecuteProcedureQualifier(self, ctx:Cypher5Parser.ExecuteProcedureQualifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#settingQualifier.
    def visitSettingQualifier(self, ctx:Cypher5Parser.SettingQualifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#globs.
    def visitGlobs(self, ctx:Cypher5Parser.GlobsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#glob.
    def visitGlob(self, ctx:Cypher5Parser.GlobContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#globRecursive.
    def visitGlobRecursive(self, ctx:Cypher5Parser.GlobRecursiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#globPart.
    def visitGlobPart(self, ctx:Cypher5Parser.GlobPartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#qualifiedGraphPrivilegesWithProperty.
    def visitQualifiedGraphPrivilegesWithProperty(self, ctx:Cypher5Parser.QualifiedGraphPrivilegesWithPropertyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#qualifiedGraphPrivileges.
    def visitQualifiedGraphPrivileges(self, ctx:Cypher5Parser.QualifiedGraphPrivilegesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#labelsResource.
    def visitLabelsResource(self, ctx:Cypher5Parser.LabelsResourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#propertiesResource.
    def visitPropertiesResource(self, ctx:Cypher5Parser.PropertiesResourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#nonEmptyStringList.
    def visitNonEmptyStringList(self, ctx:Cypher5Parser.NonEmptyStringListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#graphQualifier.
    def visitGraphQualifier(self, ctx:Cypher5Parser.GraphQualifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#graphQualifierToken.
    def visitGraphQualifierToken(self, ctx:Cypher5Parser.GraphQualifierTokenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#relToken.
    def visitRelToken(self, ctx:Cypher5Parser.RelTokenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#elementToken.
    def visitElementToken(self, ctx:Cypher5Parser.ElementTokenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#nodeToken.
    def visitNodeToken(self, ctx:Cypher5Parser.NodeTokenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#databaseScope.
    def visitDatabaseScope(self, ctx:Cypher5Parser.DatabaseScopeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#graphScope.
    def visitGraphScope(self, ctx:Cypher5Parser.GraphScopeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#createCompositeDatabase.
    def visitCreateCompositeDatabase(self, ctx:Cypher5Parser.CreateCompositeDatabaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#createDatabase.
    def visitCreateDatabase(self, ctx:Cypher5Parser.CreateDatabaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#primaryTopology.
    def visitPrimaryTopology(self, ctx:Cypher5Parser.PrimaryTopologyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#primaryToken.
    def visitPrimaryToken(self, ctx:Cypher5Parser.PrimaryTokenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#secondaryTopology.
    def visitSecondaryTopology(self, ctx:Cypher5Parser.SecondaryTopologyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#secondaryToken.
    def visitSecondaryToken(self, ctx:Cypher5Parser.SecondaryTokenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#defaultLanguageSpecification.
    def visitDefaultLanguageSpecification(self, ctx:Cypher5Parser.DefaultLanguageSpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#dropDatabase.
    def visitDropDatabase(self, ctx:Cypher5Parser.DropDatabaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#aliasAction.
    def visitAliasAction(self, ctx:Cypher5Parser.AliasActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#alterDatabase.
    def visitAlterDatabase(self, ctx:Cypher5Parser.AlterDatabaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#alterDatabaseAccess.
    def visitAlterDatabaseAccess(self, ctx:Cypher5Parser.AlterDatabaseAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#alterDatabaseTopology.
    def visitAlterDatabaseTopology(self, ctx:Cypher5Parser.AlterDatabaseTopologyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#alterDatabaseOption.
    def visitAlterDatabaseOption(self, ctx:Cypher5Parser.AlterDatabaseOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#startDatabase.
    def visitStartDatabase(self, ctx:Cypher5Parser.StartDatabaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#stopDatabase.
    def visitStopDatabase(self, ctx:Cypher5Parser.StopDatabaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#waitClause.
    def visitWaitClause(self, ctx:Cypher5Parser.WaitClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#secondsToken.
    def visitSecondsToken(self, ctx:Cypher5Parser.SecondsTokenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#showDatabase.
    def visitShowDatabase(self, ctx:Cypher5Parser.ShowDatabaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#aliasName.
    def visitAliasName(self, ctx:Cypher5Parser.AliasNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#databaseName.
    def visitDatabaseName(self, ctx:Cypher5Parser.DatabaseNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#createAlias.
    def visitCreateAlias(self, ctx:Cypher5Parser.CreateAliasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#dropAlias.
    def visitDropAlias(self, ctx:Cypher5Parser.DropAliasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#alterAlias.
    def visitAlterAlias(self, ctx:Cypher5Parser.AlterAliasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#alterAliasTarget.
    def visitAlterAliasTarget(self, ctx:Cypher5Parser.AlterAliasTargetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#alterAliasUser.
    def visitAlterAliasUser(self, ctx:Cypher5Parser.AlterAliasUserContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#alterAliasPassword.
    def visitAlterAliasPassword(self, ctx:Cypher5Parser.AlterAliasPasswordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#alterAliasDriver.
    def visitAlterAliasDriver(self, ctx:Cypher5Parser.AlterAliasDriverContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#alterAliasProperties.
    def visitAlterAliasProperties(self, ctx:Cypher5Parser.AlterAliasPropertiesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#showAliases.
    def visitShowAliases(self, ctx:Cypher5Parser.ShowAliasesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#commandNameExpression.
    def visitCommandNameExpression(self, ctx:Cypher5Parser.CommandNameExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#symbolicNameOrStringParameterList.
    def visitSymbolicNameOrStringParameterList(self, ctx:Cypher5Parser.SymbolicNameOrStringParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#symbolicAliasNameList.
    def visitSymbolicAliasNameList(self, ctx:Cypher5Parser.SymbolicAliasNameListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#symbolicAliasNameOrParameter.
    def visitSymbolicAliasNameOrParameter(self, ctx:Cypher5Parser.SymbolicAliasNameOrParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#symbolicAliasName.
    def visitSymbolicAliasName(self, ctx:Cypher5Parser.SymbolicAliasNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#stringListLiteral.
    def visitStringListLiteral(self, ctx:Cypher5Parser.StringListLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#stringList.
    def visitStringList(self, ctx:Cypher5Parser.StringListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#stringLiteral.
    def visitStringLiteral(self, ctx:Cypher5Parser.StringLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#stringOrParameterExpression.
    def visitStringOrParameterExpression(self, ctx:Cypher5Parser.StringOrParameterExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#stringOrParameter.
    def visitStringOrParameter(self, ctx:Cypher5Parser.StringOrParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#uIntOrIntParameter.
    def visitUIntOrIntParameter(self, ctx:Cypher5Parser.UIntOrIntParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#mapOrParameter.
    def visitMapOrParameter(self, ctx:Cypher5Parser.MapOrParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#map.
    def visitMap(self, ctx:Cypher5Parser.MapContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#symbolicVariableNameString.
    def visitSymbolicVariableNameString(self, ctx:Cypher5Parser.SymbolicVariableNameStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#escapedSymbolicVariableNameString.
    def visitEscapedSymbolicVariableNameString(self, ctx:Cypher5Parser.EscapedSymbolicVariableNameStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#unescapedSymbolicVariableNameString.
    def visitUnescapedSymbolicVariableNameString(self, ctx:Cypher5Parser.UnescapedSymbolicVariableNameStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#symbolicNameString.
    def visitSymbolicNameString(self, ctx:Cypher5Parser.SymbolicNameStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#escapedSymbolicNameString.
    def visitEscapedSymbolicNameString(self, ctx:Cypher5Parser.EscapedSymbolicNameStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#unescapedSymbolicNameString.
    def visitUnescapedSymbolicNameString(self, ctx:Cypher5Parser.UnescapedSymbolicNameStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#symbolicLabelNameString.
    def visitSymbolicLabelNameString(self, ctx:Cypher5Parser.SymbolicLabelNameStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#unescapedLabelSymbolicNameString.
    def visitUnescapedLabelSymbolicNameString(self, ctx:Cypher5Parser.UnescapedLabelSymbolicNameStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#unescapedLabelSymbolicNameString_.
    def visitUnescapedLabelSymbolicNameString_(self, ctx:Cypher5Parser.UnescapedLabelSymbolicNameString_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cypher5Parser#endOfFile.
    def visitEndOfFile(self, ctx:Cypher5Parser.EndOfFileContext):
        return self.visitChildren(ctx)



del Cypher5Parser