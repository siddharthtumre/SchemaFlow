# Generated from grammar/Cypher5Parser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .Cypher5Parser import Cypher5Parser
else:
    from Cypher5Parser import Cypher5Parser

# This class defines a complete listener for a parse tree produced by Cypher5Parser.
class Cypher5ParserListener(ParseTreeListener):

    # Enter a parse tree produced by Cypher5Parser#statements.
    def enterStatements(self, ctx:Cypher5Parser.StatementsContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#statements.
    def exitStatements(self, ctx:Cypher5Parser.StatementsContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#statement.
    def enterStatement(self, ctx:Cypher5Parser.StatementContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#statement.
    def exitStatement(self, ctx:Cypher5Parser.StatementContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#periodicCommitQueryHintFailure.
    def enterPeriodicCommitQueryHintFailure(self, ctx:Cypher5Parser.PeriodicCommitQueryHintFailureContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#periodicCommitQueryHintFailure.
    def exitPeriodicCommitQueryHintFailure(self, ctx:Cypher5Parser.PeriodicCommitQueryHintFailureContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#regularQuery.
    def enterRegularQuery(self, ctx:Cypher5Parser.RegularQueryContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#regularQuery.
    def exitRegularQuery(self, ctx:Cypher5Parser.RegularQueryContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#singleQuery.
    def enterSingleQuery(self, ctx:Cypher5Parser.SingleQueryContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#singleQuery.
    def exitSingleQuery(self, ctx:Cypher5Parser.SingleQueryContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#clause.
    def enterClause(self, ctx:Cypher5Parser.ClauseContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#clause.
    def exitClause(self, ctx:Cypher5Parser.ClauseContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#useClause.
    def enterUseClause(self, ctx:Cypher5Parser.UseClauseContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#useClause.
    def exitUseClause(self, ctx:Cypher5Parser.UseClauseContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#graphReference.
    def enterGraphReference(self, ctx:Cypher5Parser.GraphReferenceContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#graphReference.
    def exitGraphReference(self, ctx:Cypher5Parser.GraphReferenceContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#finishClause.
    def enterFinishClause(self, ctx:Cypher5Parser.FinishClauseContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#finishClause.
    def exitFinishClause(self, ctx:Cypher5Parser.FinishClauseContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#returnClause.
    def enterReturnClause(self, ctx:Cypher5Parser.ReturnClauseContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#returnClause.
    def exitReturnClause(self, ctx:Cypher5Parser.ReturnClauseContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#returnBody.
    def enterReturnBody(self, ctx:Cypher5Parser.ReturnBodyContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#returnBody.
    def exitReturnBody(self, ctx:Cypher5Parser.ReturnBodyContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#returnItem.
    def enterReturnItem(self, ctx:Cypher5Parser.ReturnItemContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#returnItem.
    def exitReturnItem(self, ctx:Cypher5Parser.ReturnItemContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#returnItems.
    def enterReturnItems(self, ctx:Cypher5Parser.ReturnItemsContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#returnItems.
    def exitReturnItems(self, ctx:Cypher5Parser.ReturnItemsContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#orderItem.
    def enterOrderItem(self, ctx:Cypher5Parser.OrderItemContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#orderItem.
    def exitOrderItem(self, ctx:Cypher5Parser.OrderItemContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#ascToken.
    def enterAscToken(self, ctx:Cypher5Parser.AscTokenContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#ascToken.
    def exitAscToken(self, ctx:Cypher5Parser.AscTokenContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#descToken.
    def enterDescToken(self, ctx:Cypher5Parser.DescTokenContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#descToken.
    def exitDescToken(self, ctx:Cypher5Parser.DescTokenContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#orderBy.
    def enterOrderBy(self, ctx:Cypher5Parser.OrderByContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#orderBy.
    def exitOrderBy(self, ctx:Cypher5Parser.OrderByContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#skip.
    def enterSkip(self, ctx:Cypher5Parser.SkipContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#skip.
    def exitSkip(self, ctx:Cypher5Parser.SkipContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#limit.
    def enterLimit(self, ctx:Cypher5Parser.LimitContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#limit.
    def exitLimit(self, ctx:Cypher5Parser.LimitContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#whereClause.
    def enterWhereClause(self, ctx:Cypher5Parser.WhereClauseContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#whereClause.
    def exitWhereClause(self, ctx:Cypher5Parser.WhereClauseContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#withClause.
    def enterWithClause(self, ctx:Cypher5Parser.WithClauseContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#withClause.
    def exitWithClause(self, ctx:Cypher5Parser.WithClauseContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#createClause.
    def enterCreateClause(self, ctx:Cypher5Parser.CreateClauseContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#createClause.
    def exitCreateClause(self, ctx:Cypher5Parser.CreateClauseContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#insertClause.
    def enterInsertClause(self, ctx:Cypher5Parser.InsertClauseContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#insertClause.
    def exitInsertClause(self, ctx:Cypher5Parser.InsertClauseContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#setClause.
    def enterSetClause(self, ctx:Cypher5Parser.SetClauseContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#setClause.
    def exitSetClause(self, ctx:Cypher5Parser.SetClauseContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#SetProp.
    def enterSetProp(self, ctx:Cypher5Parser.SetPropContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#SetProp.
    def exitSetProp(self, ctx:Cypher5Parser.SetPropContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#SetDynamicProp.
    def enterSetDynamicProp(self, ctx:Cypher5Parser.SetDynamicPropContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#SetDynamicProp.
    def exitSetDynamicProp(self, ctx:Cypher5Parser.SetDynamicPropContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#SetProps.
    def enterSetProps(self, ctx:Cypher5Parser.SetPropsContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#SetProps.
    def exitSetProps(self, ctx:Cypher5Parser.SetPropsContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#AddProp.
    def enterAddProp(self, ctx:Cypher5Parser.AddPropContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#AddProp.
    def exitAddProp(self, ctx:Cypher5Parser.AddPropContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#SetLabels.
    def enterSetLabels(self, ctx:Cypher5Parser.SetLabelsContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#SetLabels.
    def exitSetLabels(self, ctx:Cypher5Parser.SetLabelsContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#SetLabelsIs.
    def enterSetLabelsIs(self, ctx:Cypher5Parser.SetLabelsIsContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#SetLabelsIs.
    def exitSetLabelsIs(self, ctx:Cypher5Parser.SetLabelsIsContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#removeClause.
    def enterRemoveClause(self, ctx:Cypher5Parser.RemoveClauseContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#removeClause.
    def exitRemoveClause(self, ctx:Cypher5Parser.RemoveClauseContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#RemoveProp.
    def enterRemoveProp(self, ctx:Cypher5Parser.RemovePropContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#RemoveProp.
    def exitRemoveProp(self, ctx:Cypher5Parser.RemovePropContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#RemoveDynamicProp.
    def enterRemoveDynamicProp(self, ctx:Cypher5Parser.RemoveDynamicPropContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#RemoveDynamicProp.
    def exitRemoveDynamicProp(self, ctx:Cypher5Parser.RemoveDynamicPropContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#RemoveLabels.
    def enterRemoveLabels(self, ctx:Cypher5Parser.RemoveLabelsContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#RemoveLabels.
    def exitRemoveLabels(self, ctx:Cypher5Parser.RemoveLabelsContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#RemoveLabelsIs.
    def enterRemoveLabelsIs(self, ctx:Cypher5Parser.RemoveLabelsIsContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#RemoveLabelsIs.
    def exitRemoveLabelsIs(self, ctx:Cypher5Parser.RemoveLabelsIsContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#deleteClause.
    def enterDeleteClause(self, ctx:Cypher5Parser.DeleteClauseContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#deleteClause.
    def exitDeleteClause(self, ctx:Cypher5Parser.DeleteClauseContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#matchClause.
    def enterMatchClause(self, ctx:Cypher5Parser.MatchClauseContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#matchClause.
    def exitMatchClause(self, ctx:Cypher5Parser.MatchClauseContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#matchMode.
    def enterMatchMode(self, ctx:Cypher5Parser.MatchModeContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#matchMode.
    def exitMatchMode(self, ctx:Cypher5Parser.MatchModeContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#hint.
    def enterHint(self, ctx:Cypher5Parser.HintContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#hint.
    def exitHint(self, ctx:Cypher5Parser.HintContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#expandHintStep.
    def enterExpandHintStep(self, ctx:Cypher5Parser.ExpandHintStepContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#expandHintStep.
    def exitExpandHintStep(self, ctx:Cypher5Parser.ExpandHintStepContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#mergeClause.
    def enterMergeClause(self, ctx:Cypher5Parser.MergeClauseContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#mergeClause.
    def exitMergeClause(self, ctx:Cypher5Parser.MergeClauseContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#mergeAction.
    def enterMergeAction(self, ctx:Cypher5Parser.MergeActionContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#mergeAction.
    def exitMergeAction(self, ctx:Cypher5Parser.MergeActionContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#unwindClause.
    def enterUnwindClause(self, ctx:Cypher5Parser.UnwindClauseContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#unwindClause.
    def exitUnwindClause(self, ctx:Cypher5Parser.UnwindClauseContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#callClause.
    def enterCallClause(self, ctx:Cypher5Parser.CallClauseContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#callClause.
    def exitCallClause(self, ctx:Cypher5Parser.CallClauseContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#procedureName.
    def enterProcedureName(self, ctx:Cypher5Parser.ProcedureNameContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#procedureName.
    def exitProcedureName(self, ctx:Cypher5Parser.ProcedureNameContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#procedureArgument.
    def enterProcedureArgument(self, ctx:Cypher5Parser.ProcedureArgumentContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#procedureArgument.
    def exitProcedureArgument(self, ctx:Cypher5Parser.ProcedureArgumentContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#procedureResultItem.
    def enterProcedureResultItem(self, ctx:Cypher5Parser.ProcedureResultItemContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#procedureResultItem.
    def exitProcedureResultItem(self, ctx:Cypher5Parser.ProcedureResultItemContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#loadCSVClause.
    def enterLoadCSVClause(self, ctx:Cypher5Parser.LoadCSVClauseContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#loadCSVClause.
    def exitLoadCSVClause(self, ctx:Cypher5Parser.LoadCSVClauseContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#foreachClause.
    def enterForeachClause(self, ctx:Cypher5Parser.ForeachClauseContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#foreachClause.
    def exitForeachClause(self, ctx:Cypher5Parser.ForeachClauseContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#subqueryClause.
    def enterSubqueryClause(self, ctx:Cypher5Parser.SubqueryClauseContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#subqueryClause.
    def exitSubqueryClause(self, ctx:Cypher5Parser.SubqueryClauseContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#subqueryScope.
    def enterSubqueryScope(self, ctx:Cypher5Parser.SubqueryScopeContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#subqueryScope.
    def exitSubqueryScope(self, ctx:Cypher5Parser.SubqueryScopeContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#subqueryInTransactionsParameters.
    def enterSubqueryInTransactionsParameters(self, ctx:Cypher5Parser.SubqueryInTransactionsParametersContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#subqueryInTransactionsParameters.
    def exitSubqueryInTransactionsParameters(self, ctx:Cypher5Parser.SubqueryInTransactionsParametersContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#subqueryInTransactionsBatchParameters.
    def enterSubqueryInTransactionsBatchParameters(self, ctx:Cypher5Parser.SubqueryInTransactionsBatchParametersContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#subqueryInTransactionsBatchParameters.
    def exitSubqueryInTransactionsBatchParameters(self, ctx:Cypher5Parser.SubqueryInTransactionsBatchParametersContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#subqueryInTransactionsErrorParameters.
    def enterSubqueryInTransactionsErrorParameters(self, ctx:Cypher5Parser.SubqueryInTransactionsErrorParametersContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#subqueryInTransactionsErrorParameters.
    def exitSubqueryInTransactionsErrorParameters(self, ctx:Cypher5Parser.SubqueryInTransactionsErrorParametersContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#subqueryInTransactionsRetryParameters.
    def enterSubqueryInTransactionsRetryParameters(self, ctx:Cypher5Parser.SubqueryInTransactionsRetryParametersContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#subqueryInTransactionsRetryParameters.
    def exitSubqueryInTransactionsRetryParameters(self, ctx:Cypher5Parser.SubqueryInTransactionsRetryParametersContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#subqueryInTransactionsReportParameters.
    def enterSubqueryInTransactionsReportParameters(self, ctx:Cypher5Parser.SubqueryInTransactionsReportParametersContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#subqueryInTransactionsReportParameters.
    def exitSubqueryInTransactionsReportParameters(self, ctx:Cypher5Parser.SubqueryInTransactionsReportParametersContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#orderBySkipLimitClause.
    def enterOrderBySkipLimitClause(self, ctx:Cypher5Parser.OrderBySkipLimitClauseContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#orderBySkipLimitClause.
    def exitOrderBySkipLimitClause(self, ctx:Cypher5Parser.OrderBySkipLimitClauseContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#patternList.
    def enterPatternList(self, ctx:Cypher5Parser.PatternListContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#patternList.
    def exitPatternList(self, ctx:Cypher5Parser.PatternListContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#insertPatternList.
    def enterInsertPatternList(self, ctx:Cypher5Parser.InsertPatternListContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#insertPatternList.
    def exitInsertPatternList(self, ctx:Cypher5Parser.InsertPatternListContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#pattern.
    def enterPattern(self, ctx:Cypher5Parser.PatternContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#pattern.
    def exitPattern(self, ctx:Cypher5Parser.PatternContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#insertPattern.
    def enterInsertPattern(self, ctx:Cypher5Parser.InsertPatternContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#insertPattern.
    def exitInsertPattern(self, ctx:Cypher5Parser.InsertPatternContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#quantifier.
    def enterQuantifier(self, ctx:Cypher5Parser.QuantifierContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#quantifier.
    def exitQuantifier(self, ctx:Cypher5Parser.QuantifierContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#anonymousPattern.
    def enterAnonymousPattern(self, ctx:Cypher5Parser.AnonymousPatternContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#anonymousPattern.
    def exitAnonymousPattern(self, ctx:Cypher5Parser.AnonymousPatternContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#shortestPathPattern.
    def enterShortestPathPattern(self, ctx:Cypher5Parser.ShortestPathPatternContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#shortestPathPattern.
    def exitShortestPathPattern(self, ctx:Cypher5Parser.ShortestPathPatternContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#patternElement.
    def enterPatternElement(self, ctx:Cypher5Parser.PatternElementContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#patternElement.
    def exitPatternElement(self, ctx:Cypher5Parser.PatternElementContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#AnyShortestPath.
    def enterAnyShortestPath(self, ctx:Cypher5Parser.AnyShortestPathContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#AnyShortestPath.
    def exitAnyShortestPath(self, ctx:Cypher5Parser.AnyShortestPathContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#AllShortestPath.
    def enterAllShortestPath(self, ctx:Cypher5Parser.AllShortestPathContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#AllShortestPath.
    def exitAllShortestPath(self, ctx:Cypher5Parser.AllShortestPathContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#AnyPath.
    def enterAnyPath(self, ctx:Cypher5Parser.AnyPathContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#AnyPath.
    def exitAnyPath(self, ctx:Cypher5Parser.AnyPathContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#AllPath.
    def enterAllPath(self, ctx:Cypher5Parser.AllPathContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#AllPath.
    def exitAllPath(self, ctx:Cypher5Parser.AllPathContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#ShortestGroup.
    def enterShortestGroup(self, ctx:Cypher5Parser.ShortestGroupContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#ShortestGroup.
    def exitShortestGroup(self, ctx:Cypher5Parser.ShortestGroupContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#groupToken.
    def enterGroupToken(self, ctx:Cypher5Parser.GroupTokenContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#groupToken.
    def exitGroupToken(self, ctx:Cypher5Parser.GroupTokenContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#pathToken.
    def enterPathToken(self, ctx:Cypher5Parser.PathTokenContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#pathToken.
    def exitPathToken(self, ctx:Cypher5Parser.PathTokenContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#pathPatternNonEmpty.
    def enterPathPatternNonEmpty(self, ctx:Cypher5Parser.PathPatternNonEmptyContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#pathPatternNonEmpty.
    def exitPathPatternNonEmpty(self, ctx:Cypher5Parser.PathPatternNonEmptyContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#nodePattern.
    def enterNodePattern(self, ctx:Cypher5Parser.NodePatternContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#nodePattern.
    def exitNodePattern(self, ctx:Cypher5Parser.NodePatternContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#insertNodePattern.
    def enterInsertNodePattern(self, ctx:Cypher5Parser.InsertNodePatternContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#insertNodePattern.
    def exitInsertNodePattern(self, ctx:Cypher5Parser.InsertNodePatternContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#parenthesizedPath.
    def enterParenthesizedPath(self, ctx:Cypher5Parser.ParenthesizedPathContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#parenthesizedPath.
    def exitParenthesizedPath(self, ctx:Cypher5Parser.ParenthesizedPathContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#nodeLabels.
    def enterNodeLabels(self, ctx:Cypher5Parser.NodeLabelsContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#nodeLabels.
    def exitNodeLabels(self, ctx:Cypher5Parser.NodeLabelsContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#nodeLabelsIs.
    def enterNodeLabelsIs(self, ctx:Cypher5Parser.NodeLabelsIsContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#nodeLabelsIs.
    def exitNodeLabelsIs(self, ctx:Cypher5Parser.NodeLabelsIsContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#dynamicExpression.
    def enterDynamicExpression(self, ctx:Cypher5Parser.DynamicExpressionContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#dynamicExpression.
    def exitDynamicExpression(self, ctx:Cypher5Parser.DynamicExpressionContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#dynamicAnyAllExpression.
    def enterDynamicAnyAllExpression(self, ctx:Cypher5Parser.DynamicAnyAllExpressionContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#dynamicAnyAllExpression.
    def exitDynamicAnyAllExpression(self, ctx:Cypher5Parser.DynamicAnyAllExpressionContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#dynamicLabelType.
    def enterDynamicLabelType(self, ctx:Cypher5Parser.DynamicLabelTypeContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#dynamicLabelType.
    def exitDynamicLabelType(self, ctx:Cypher5Parser.DynamicLabelTypeContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#labelType.
    def enterLabelType(self, ctx:Cypher5Parser.LabelTypeContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#labelType.
    def exitLabelType(self, ctx:Cypher5Parser.LabelTypeContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#relType.
    def enterRelType(self, ctx:Cypher5Parser.RelTypeContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#relType.
    def exitRelType(self, ctx:Cypher5Parser.RelTypeContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#labelOrRelType.
    def enterLabelOrRelType(self, ctx:Cypher5Parser.LabelOrRelTypeContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#labelOrRelType.
    def exitLabelOrRelType(self, ctx:Cypher5Parser.LabelOrRelTypeContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#properties.
    def enterProperties(self, ctx:Cypher5Parser.PropertiesContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#properties.
    def exitProperties(self, ctx:Cypher5Parser.PropertiesContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#relationshipPattern.
    def enterRelationshipPattern(self, ctx:Cypher5Parser.RelationshipPatternContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#relationshipPattern.
    def exitRelationshipPattern(self, ctx:Cypher5Parser.RelationshipPatternContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#insertRelationshipPattern.
    def enterInsertRelationshipPattern(self, ctx:Cypher5Parser.InsertRelationshipPatternContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#insertRelationshipPattern.
    def exitInsertRelationshipPattern(self, ctx:Cypher5Parser.InsertRelationshipPatternContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#leftArrow.
    def enterLeftArrow(self, ctx:Cypher5Parser.LeftArrowContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#leftArrow.
    def exitLeftArrow(self, ctx:Cypher5Parser.LeftArrowContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#arrowLine.
    def enterArrowLine(self, ctx:Cypher5Parser.ArrowLineContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#arrowLine.
    def exitArrowLine(self, ctx:Cypher5Parser.ArrowLineContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#rightArrow.
    def enterRightArrow(self, ctx:Cypher5Parser.RightArrowContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#rightArrow.
    def exitRightArrow(self, ctx:Cypher5Parser.RightArrowContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#pathLength.
    def enterPathLength(self, ctx:Cypher5Parser.PathLengthContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#pathLength.
    def exitPathLength(self, ctx:Cypher5Parser.PathLengthContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#labelExpression.
    def enterLabelExpression(self, ctx:Cypher5Parser.LabelExpressionContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#labelExpression.
    def exitLabelExpression(self, ctx:Cypher5Parser.LabelExpressionContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#labelExpression4.
    def enterLabelExpression4(self, ctx:Cypher5Parser.LabelExpression4Context):
        pass

    # Exit a parse tree produced by Cypher5Parser#labelExpression4.
    def exitLabelExpression4(self, ctx:Cypher5Parser.LabelExpression4Context):
        pass


    # Enter a parse tree produced by Cypher5Parser#labelExpression4Is.
    def enterLabelExpression4Is(self, ctx:Cypher5Parser.LabelExpression4IsContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#labelExpression4Is.
    def exitLabelExpression4Is(self, ctx:Cypher5Parser.LabelExpression4IsContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#labelExpression3.
    def enterLabelExpression3(self, ctx:Cypher5Parser.LabelExpression3Context):
        pass

    # Exit a parse tree produced by Cypher5Parser#labelExpression3.
    def exitLabelExpression3(self, ctx:Cypher5Parser.LabelExpression3Context):
        pass


    # Enter a parse tree produced by Cypher5Parser#labelExpression3Is.
    def enterLabelExpression3Is(self, ctx:Cypher5Parser.LabelExpression3IsContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#labelExpression3Is.
    def exitLabelExpression3Is(self, ctx:Cypher5Parser.LabelExpression3IsContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#labelExpression2.
    def enterLabelExpression2(self, ctx:Cypher5Parser.LabelExpression2Context):
        pass

    # Exit a parse tree produced by Cypher5Parser#labelExpression2.
    def exitLabelExpression2(self, ctx:Cypher5Parser.LabelExpression2Context):
        pass


    # Enter a parse tree produced by Cypher5Parser#labelExpression2Is.
    def enterLabelExpression2Is(self, ctx:Cypher5Parser.LabelExpression2IsContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#labelExpression2Is.
    def exitLabelExpression2Is(self, ctx:Cypher5Parser.LabelExpression2IsContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#ParenthesizedLabelExpression.
    def enterParenthesizedLabelExpression(self, ctx:Cypher5Parser.ParenthesizedLabelExpressionContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#ParenthesizedLabelExpression.
    def exitParenthesizedLabelExpression(self, ctx:Cypher5Parser.ParenthesizedLabelExpressionContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#AnyLabel.
    def enterAnyLabel(self, ctx:Cypher5Parser.AnyLabelContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#AnyLabel.
    def exitAnyLabel(self, ctx:Cypher5Parser.AnyLabelContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#DynamicLabel.
    def enterDynamicLabel(self, ctx:Cypher5Parser.DynamicLabelContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#DynamicLabel.
    def exitDynamicLabel(self, ctx:Cypher5Parser.DynamicLabelContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#LabelName.
    def enterLabelName(self, ctx:Cypher5Parser.LabelNameContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#LabelName.
    def exitLabelName(self, ctx:Cypher5Parser.LabelNameContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#ParenthesizedLabelExpressionIs.
    def enterParenthesizedLabelExpressionIs(self, ctx:Cypher5Parser.ParenthesizedLabelExpressionIsContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#ParenthesizedLabelExpressionIs.
    def exitParenthesizedLabelExpressionIs(self, ctx:Cypher5Parser.ParenthesizedLabelExpressionIsContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#AnyLabelIs.
    def enterAnyLabelIs(self, ctx:Cypher5Parser.AnyLabelIsContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#AnyLabelIs.
    def exitAnyLabelIs(self, ctx:Cypher5Parser.AnyLabelIsContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#DynamicLabelIs.
    def enterDynamicLabelIs(self, ctx:Cypher5Parser.DynamicLabelIsContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#DynamicLabelIs.
    def exitDynamicLabelIs(self, ctx:Cypher5Parser.DynamicLabelIsContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#LabelNameIs.
    def enterLabelNameIs(self, ctx:Cypher5Parser.LabelNameIsContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#LabelNameIs.
    def exitLabelNameIs(self, ctx:Cypher5Parser.LabelNameIsContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#insertNodeLabelExpression.
    def enterInsertNodeLabelExpression(self, ctx:Cypher5Parser.InsertNodeLabelExpressionContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#insertNodeLabelExpression.
    def exitInsertNodeLabelExpression(self, ctx:Cypher5Parser.InsertNodeLabelExpressionContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#insertRelationshipLabelExpression.
    def enterInsertRelationshipLabelExpression(self, ctx:Cypher5Parser.InsertRelationshipLabelExpressionContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#insertRelationshipLabelExpression.
    def exitInsertRelationshipLabelExpression(self, ctx:Cypher5Parser.InsertRelationshipLabelExpressionContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#expression.
    def enterExpression(self, ctx:Cypher5Parser.ExpressionContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#expression.
    def exitExpression(self, ctx:Cypher5Parser.ExpressionContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#expression11.
    def enterExpression11(self, ctx:Cypher5Parser.Expression11Context):
        pass

    # Exit a parse tree produced by Cypher5Parser#expression11.
    def exitExpression11(self, ctx:Cypher5Parser.Expression11Context):
        pass


    # Enter a parse tree produced by Cypher5Parser#expression10.
    def enterExpression10(self, ctx:Cypher5Parser.Expression10Context):
        pass

    # Exit a parse tree produced by Cypher5Parser#expression10.
    def exitExpression10(self, ctx:Cypher5Parser.Expression10Context):
        pass


    # Enter a parse tree produced by Cypher5Parser#expression9.
    def enterExpression9(self, ctx:Cypher5Parser.Expression9Context):
        pass

    # Exit a parse tree produced by Cypher5Parser#expression9.
    def exitExpression9(self, ctx:Cypher5Parser.Expression9Context):
        pass


    # Enter a parse tree produced by Cypher5Parser#expression8.
    def enterExpression8(self, ctx:Cypher5Parser.Expression8Context):
        pass

    # Exit a parse tree produced by Cypher5Parser#expression8.
    def exitExpression8(self, ctx:Cypher5Parser.Expression8Context):
        pass


    # Enter a parse tree produced by Cypher5Parser#expression7.
    def enterExpression7(self, ctx:Cypher5Parser.Expression7Context):
        pass

    # Exit a parse tree produced by Cypher5Parser#expression7.
    def exitExpression7(self, ctx:Cypher5Parser.Expression7Context):
        pass


    # Enter a parse tree produced by Cypher5Parser#StringAndListComparison.
    def enterStringAndListComparison(self, ctx:Cypher5Parser.StringAndListComparisonContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#StringAndListComparison.
    def exitStringAndListComparison(self, ctx:Cypher5Parser.StringAndListComparisonContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#NullComparison.
    def enterNullComparison(self, ctx:Cypher5Parser.NullComparisonContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#NullComparison.
    def exitNullComparison(self, ctx:Cypher5Parser.NullComparisonContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#TypeComparison.
    def enterTypeComparison(self, ctx:Cypher5Parser.TypeComparisonContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#TypeComparison.
    def exitTypeComparison(self, ctx:Cypher5Parser.TypeComparisonContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#NormalFormComparison.
    def enterNormalFormComparison(self, ctx:Cypher5Parser.NormalFormComparisonContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#NormalFormComparison.
    def exitNormalFormComparison(self, ctx:Cypher5Parser.NormalFormComparisonContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#normalForm.
    def enterNormalForm(self, ctx:Cypher5Parser.NormalFormContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#normalForm.
    def exitNormalForm(self, ctx:Cypher5Parser.NormalFormContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#expression6.
    def enterExpression6(self, ctx:Cypher5Parser.Expression6Context):
        pass

    # Exit a parse tree produced by Cypher5Parser#expression6.
    def exitExpression6(self, ctx:Cypher5Parser.Expression6Context):
        pass


    # Enter a parse tree produced by Cypher5Parser#expression5.
    def enterExpression5(self, ctx:Cypher5Parser.Expression5Context):
        pass

    # Exit a parse tree produced by Cypher5Parser#expression5.
    def exitExpression5(self, ctx:Cypher5Parser.Expression5Context):
        pass


    # Enter a parse tree produced by Cypher5Parser#expression4.
    def enterExpression4(self, ctx:Cypher5Parser.Expression4Context):
        pass

    # Exit a parse tree produced by Cypher5Parser#expression4.
    def exitExpression4(self, ctx:Cypher5Parser.Expression4Context):
        pass


    # Enter a parse tree produced by Cypher5Parser#expression3.
    def enterExpression3(self, ctx:Cypher5Parser.Expression3Context):
        pass

    # Exit a parse tree produced by Cypher5Parser#expression3.
    def exitExpression3(self, ctx:Cypher5Parser.Expression3Context):
        pass


    # Enter a parse tree produced by Cypher5Parser#expression2.
    def enterExpression2(self, ctx:Cypher5Parser.Expression2Context):
        pass

    # Exit a parse tree produced by Cypher5Parser#expression2.
    def exitExpression2(self, ctx:Cypher5Parser.Expression2Context):
        pass


    # Enter a parse tree produced by Cypher5Parser#PropertyPostfix.
    def enterPropertyPostfix(self, ctx:Cypher5Parser.PropertyPostfixContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#PropertyPostfix.
    def exitPropertyPostfix(self, ctx:Cypher5Parser.PropertyPostfixContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#LabelPostfix.
    def enterLabelPostfix(self, ctx:Cypher5Parser.LabelPostfixContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#LabelPostfix.
    def exitLabelPostfix(self, ctx:Cypher5Parser.LabelPostfixContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#IndexPostfix.
    def enterIndexPostfix(self, ctx:Cypher5Parser.IndexPostfixContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#IndexPostfix.
    def exitIndexPostfix(self, ctx:Cypher5Parser.IndexPostfixContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#RangePostfix.
    def enterRangePostfix(self, ctx:Cypher5Parser.RangePostfixContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#RangePostfix.
    def exitRangePostfix(self, ctx:Cypher5Parser.RangePostfixContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#property.
    def enterProperty(self, ctx:Cypher5Parser.PropertyContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#property.
    def exitProperty(self, ctx:Cypher5Parser.PropertyContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#dynamicProperty.
    def enterDynamicProperty(self, ctx:Cypher5Parser.DynamicPropertyContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#dynamicProperty.
    def exitDynamicProperty(self, ctx:Cypher5Parser.DynamicPropertyContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#propertyExpression.
    def enterPropertyExpression(self, ctx:Cypher5Parser.PropertyExpressionContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#propertyExpression.
    def exitPropertyExpression(self, ctx:Cypher5Parser.PropertyExpressionContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#dynamicPropertyExpression.
    def enterDynamicPropertyExpression(self, ctx:Cypher5Parser.DynamicPropertyExpressionContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#dynamicPropertyExpression.
    def exitDynamicPropertyExpression(self, ctx:Cypher5Parser.DynamicPropertyExpressionContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#expression1.
    def enterExpression1(self, ctx:Cypher5Parser.Expression1Context):
        pass

    # Exit a parse tree produced by Cypher5Parser#expression1.
    def exitExpression1(self, ctx:Cypher5Parser.Expression1Context):
        pass


    # Enter a parse tree produced by Cypher5Parser#NumericLiteral.
    def enterNumericLiteral(self, ctx:Cypher5Parser.NumericLiteralContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#NumericLiteral.
    def exitNumericLiteral(self, ctx:Cypher5Parser.NumericLiteralContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#StringsLiteral.
    def enterStringsLiteral(self, ctx:Cypher5Parser.StringsLiteralContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#StringsLiteral.
    def exitStringsLiteral(self, ctx:Cypher5Parser.StringsLiteralContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#OtherLiteral.
    def enterOtherLiteral(self, ctx:Cypher5Parser.OtherLiteralContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#OtherLiteral.
    def exitOtherLiteral(self, ctx:Cypher5Parser.OtherLiteralContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#BooleanLiteral.
    def enterBooleanLiteral(self, ctx:Cypher5Parser.BooleanLiteralContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#BooleanLiteral.
    def exitBooleanLiteral(self, ctx:Cypher5Parser.BooleanLiteralContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#KeywordLiteral.
    def enterKeywordLiteral(self, ctx:Cypher5Parser.KeywordLiteralContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#KeywordLiteral.
    def exitKeywordLiteral(self, ctx:Cypher5Parser.KeywordLiteralContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#caseExpression.
    def enterCaseExpression(self, ctx:Cypher5Parser.CaseExpressionContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#caseExpression.
    def exitCaseExpression(self, ctx:Cypher5Parser.CaseExpressionContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#caseAlternative.
    def enterCaseAlternative(self, ctx:Cypher5Parser.CaseAlternativeContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#caseAlternative.
    def exitCaseAlternative(self, ctx:Cypher5Parser.CaseAlternativeContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#extendedCaseExpression.
    def enterExtendedCaseExpression(self, ctx:Cypher5Parser.ExtendedCaseExpressionContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#extendedCaseExpression.
    def exitExtendedCaseExpression(self, ctx:Cypher5Parser.ExtendedCaseExpressionContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#extendedCaseAlternative.
    def enterExtendedCaseAlternative(self, ctx:Cypher5Parser.ExtendedCaseAlternativeContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#extendedCaseAlternative.
    def exitExtendedCaseAlternative(self, ctx:Cypher5Parser.ExtendedCaseAlternativeContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#WhenStringOrList.
    def enterWhenStringOrList(self, ctx:Cypher5Parser.WhenStringOrListContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#WhenStringOrList.
    def exitWhenStringOrList(self, ctx:Cypher5Parser.WhenStringOrListContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#WhenNull.
    def enterWhenNull(self, ctx:Cypher5Parser.WhenNullContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#WhenNull.
    def exitWhenNull(self, ctx:Cypher5Parser.WhenNullContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#WhenType.
    def enterWhenType(self, ctx:Cypher5Parser.WhenTypeContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#WhenType.
    def exitWhenType(self, ctx:Cypher5Parser.WhenTypeContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#WhenForm.
    def enterWhenForm(self, ctx:Cypher5Parser.WhenFormContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#WhenForm.
    def exitWhenForm(self, ctx:Cypher5Parser.WhenFormContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#WhenComparator.
    def enterWhenComparator(self, ctx:Cypher5Parser.WhenComparatorContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#WhenComparator.
    def exitWhenComparator(self, ctx:Cypher5Parser.WhenComparatorContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#WhenEquals.
    def enterWhenEquals(self, ctx:Cypher5Parser.WhenEqualsContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#WhenEquals.
    def exitWhenEquals(self, ctx:Cypher5Parser.WhenEqualsContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#listComprehension.
    def enterListComprehension(self, ctx:Cypher5Parser.ListComprehensionContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#listComprehension.
    def exitListComprehension(self, ctx:Cypher5Parser.ListComprehensionContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#patternComprehension.
    def enterPatternComprehension(self, ctx:Cypher5Parser.PatternComprehensionContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#patternComprehension.
    def exitPatternComprehension(self, ctx:Cypher5Parser.PatternComprehensionContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#reduceExpression.
    def enterReduceExpression(self, ctx:Cypher5Parser.ReduceExpressionContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#reduceExpression.
    def exitReduceExpression(self, ctx:Cypher5Parser.ReduceExpressionContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#listItemsPredicate.
    def enterListItemsPredicate(self, ctx:Cypher5Parser.ListItemsPredicateContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#listItemsPredicate.
    def exitListItemsPredicate(self, ctx:Cypher5Parser.ListItemsPredicateContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#normalizeFunction.
    def enterNormalizeFunction(self, ctx:Cypher5Parser.NormalizeFunctionContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#normalizeFunction.
    def exitNormalizeFunction(self, ctx:Cypher5Parser.NormalizeFunctionContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#trimFunction.
    def enterTrimFunction(self, ctx:Cypher5Parser.TrimFunctionContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#trimFunction.
    def exitTrimFunction(self, ctx:Cypher5Parser.TrimFunctionContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#patternExpression.
    def enterPatternExpression(self, ctx:Cypher5Parser.PatternExpressionContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#patternExpression.
    def exitPatternExpression(self, ctx:Cypher5Parser.PatternExpressionContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#shortestPathExpression.
    def enterShortestPathExpression(self, ctx:Cypher5Parser.ShortestPathExpressionContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#shortestPathExpression.
    def exitShortestPathExpression(self, ctx:Cypher5Parser.ShortestPathExpressionContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#parenthesizedExpression.
    def enterParenthesizedExpression(self, ctx:Cypher5Parser.ParenthesizedExpressionContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#parenthesizedExpression.
    def exitParenthesizedExpression(self, ctx:Cypher5Parser.ParenthesizedExpressionContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#mapProjection.
    def enterMapProjection(self, ctx:Cypher5Parser.MapProjectionContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#mapProjection.
    def exitMapProjection(self, ctx:Cypher5Parser.MapProjectionContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#mapProjectionElement.
    def enterMapProjectionElement(self, ctx:Cypher5Parser.MapProjectionElementContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#mapProjectionElement.
    def exitMapProjectionElement(self, ctx:Cypher5Parser.MapProjectionElementContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#countStar.
    def enterCountStar(self, ctx:Cypher5Parser.CountStarContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#countStar.
    def exitCountStar(self, ctx:Cypher5Parser.CountStarContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#existsExpression.
    def enterExistsExpression(self, ctx:Cypher5Parser.ExistsExpressionContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#existsExpression.
    def exitExistsExpression(self, ctx:Cypher5Parser.ExistsExpressionContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#countExpression.
    def enterCountExpression(self, ctx:Cypher5Parser.CountExpressionContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#countExpression.
    def exitCountExpression(self, ctx:Cypher5Parser.CountExpressionContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#collectExpression.
    def enterCollectExpression(self, ctx:Cypher5Parser.CollectExpressionContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#collectExpression.
    def exitCollectExpression(self, ctx:Cypher5Parser.CollectExpressionContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#numberLiteral.
    def enterNumberLiteral(self, ctx:Cypher5Parser.NumberLiteralContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#numberLiteral.
    def exitNumberLiteral(self, ctx:Cypher5Parser.NumberLiteralContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#signedIntegerLiteral.
    def enterSignedIntegerLiteral(self, ctx:Cypher5Parser.SignedIntegerLiteralContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#signedIntegerLiteral.
    def exitSignedIntegerLiteral(self, ctx:Cypher5Parser.SignedIntegerLiteralContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#listLiteral.
    def enterListLiteral(self, ctx:Cypher5Parser.ListLiteralContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#listLiteral.
    def exitListLiteral(self, ctx:Cypher5Parser.ListLiteralContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#propertyKeyName.
    def enterPropertyKeyName(self, ctx:Cypher5Parser.PropertyKeyNameContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#propertyKeyName.
    def exitPropertyKeyName(self, ctx:Cypher5Parser.PropertyKeyNameContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#parameter.
    def enterParameter(self, ctx:Cypher5Parser.ParameterContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#parameter.
    def exitParameter(self, ctx:Cypher5Parser.ParameterContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#parameterName.
    def enterParameterName(self, ctx:Cypher5Parser.ParameterNameContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#parameterName.
    def exitParameterName(self, ctx:Cypher5Parser.ParameterNameContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#functionInvocation.
    def enterFunctionInvocation(self, ctx:Cypher5Parser.FunctionInvocationContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#functionInvocation.
    def exitFunctionInvocation(self, ctx:Cypher5Parser.FunctionInvocationContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#functionArgument.
    def enterFunctionArgument(self, ctx:Cypher5Parser.FunctionArgumentContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#functionArgument.
    def exitFunctionArgument(self, ctx:Cypher5Parser.FunctionArgumentContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#functionName.
    def enterFunctionName(self, ctx:Cypher5Parser.FunctionNameContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#functionName.
    def exitFunctionName(self, ctx:Cypher5Parser.FunctionNameContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#namespace.
    def enterNamespace(self, ctx:Cypher5Parser.NamespaceContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#namespace.
    def exitNamespace(self, ctx:Cypher5Parser.NamespaceContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#variable.
    def enterVariable(self, ctx:Cypher5Parser.VariableContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#variable.
    def exitVariable(self, ctx:Cypher5Parser.VariableContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#obfuscatedLiteral.
    def enterObfuscatedLiteral(self, ctx:Cypher5Parser.ObfuscatedLiteralContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#obfuscatedLiteral.
    def exitObfuscatedLiteral(self, ctx:Cypher5Parser.ObfuscatedLiteralContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#nonEmptyNameList.
    def enterNonEmptyNameList(self, ctx:Cypher5Parser.NonEmptyNameListContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#nonEmptyNameList.
    def exitNonEmptyNameList(self, ctx:Cypher5Parser.NonEmptyNameListContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#type.
    def enterType(self, ctx:Cypher5Parser.TypeContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#type.
    def exitType(self, ctx:Cypher5Parser.TypeContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#typePart.
    def enterTypePart(self, ctx:Cypher5Parser.TypePartContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#typePart.
    def exitTypePart(self, ctx:Cypher5Parser.TypePartContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#typeName.
    def enterTypeName(self, ctx:Cypher5Parser.TypeNameContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#typeName.
    def exitTypeName(self, ctx:Cypher5Parser.TypeNameContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#typeNullability.
    def enterTypeNullability(self, ctx:Cypher5Parser.TypeNullabilityContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#typeNullability.
    def exitTypeNullability(self, ctx:Cypher5Parser.TypeNullabilityContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#typeListSuffix.
    def enterTypeListSuffix(self, ctx:Cypher5Parser.TypeListSuffixContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#typeListSuffix.
    def exitTypeListSuffix(self, ctx:Cypher5Parser.TypeListSuffixContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#command.
    def enterCommand(self, ctx:Cypher5Parser.CommandContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#command.
    def exitCommand(self, ctx:Cypher5Parser.CommandContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#createCommand.
    def enterCreateCommand(self, ctx:Cypher5Parser.CreateCommandContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#createCommand.
    def exitCreateCommand(self, ctx:Cypher5Parser.CreateCommandContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#dropCommand.
    def enterDropCommand(self, ctx:Cypher5Parser.DropCommandContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#dropCommand.
    def exitDropCommand(self, ctx:Cypher5Parser.DropCommandContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#showCommand.
    def enterShowCommand(self, ctx:Cypher5Parser.ShowCommandContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#showCommand.
    def exitShowCommand(self, ctx:Cypher5Parser.ShowCommandContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#showCommandYield.
    def enterShowCommandYield(self, ctx:Cypher5Parser.ShowCommandYieldContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#showCommandYield.
    def exitShowCommandYield(self, ctx:Cypher5Parser.ShowCommandYieldContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#yieldItem.
    def enterYieldItem(self, ctx:Cypher5Parser.YieldItemContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#yieldItem.
    def exitYieldItem(self, ctx:Cypher5Parser.YieldItemContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#yieldSkip.
    def enterYieldSkip(self, ctx:Cypher5Parser.YieldSkipContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#yieldSkip.
    def exitYieldSkip(self, ctx:Cypher5Parser.YieldSkipContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#yieldLimit.
    def enterYieldLimit(self, ctx:Cypher5Parser.YieldLimitContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#yieldLimit.
    def exitYieldLimit(self, ctx:Cypher5Parser.YieldLimitContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#yieldClause.
    def enterYieldClause(self, ctx:Cypher5Parser.YieldClauseContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#yieldClause.
    def exitYieldClause(self, ctx:Cypher5Parser.YieldClauseContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#commandOptions.
    def enterCommandOptions(self, ctx:Cypher5Parser.CommandOptionsContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#commandOptions.
    def exitCommandOptions(self, ctx:Cypher5Parser.CommandOptionsContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#terminateCommand.
    def enterTerminateCommand(self, ctx:Cypher5Parser.TerminateCommandContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#terminateCommand.
    def exitTerminateCommand(self, ctx:Cypher5Parser.TerminateCommandContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#composableCommandClauses.
    def enterComposableCommandClauses(self, ctx:Cypher5Parser.ComposableCommandClausesContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#composableCommandClauses.
    def exitComposableCommandClauses(self, ctx:Cypher5Parser.ComposableCommandClausesContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#composableShowCommandClauses.
    def enterComposableShowCommandClauses(self, ctx:Cypher5Parser.ComposableShowCommandClausesContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#composableShowCommandClauses.
    def exitComposableShowCommandClauses(self, ctx:Cypher5Parser.ComposableShowCommandClausesContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#showBriefAndYield.
    def enterShowBriefAndYield(self, ctx:Cypher5Parser.ShowBriefAndYieldContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#showBriefAndYield.
    def exitShowBriefAndYield(self, ctx:Cypher5Parser.ShowBriefAndYieldContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#showIndexCommand.
    def enterShowIndexCommand(self, ctx:Cypher5Parser.ShowIndexCommandContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#showIndexCommand.
    def exitShowIndexCommand(self, ctx:Cypher5Parser.ShowIndexCommandContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#showIndexesAllowBrief.
    def enterShowIndexesAllowBrief(self, ctx:Cypher5Parser.ShowIndexesAllowBriefContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#showIndexesAllowBrief.
    def exitShowIndexesAllowBrief(self, ctx:Cypher5Parser.ShowIndexesAllowBriefContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#showIndexesNoBrief.
    def enterShowIndexesNoBrief(self, ctx:Cypher5Parser.ShowIndexesNoBriefContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#showIndexesNoBrief.
    def exitShowIndexesNoBrief(self, ctx:Cypher5Parser.ShowIndexesNoBriefContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#ShowConstraintMulti.
    def enterShowConstraintMulti(self, ctx:Cypher5Parser.ShowConstraintMultiContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#ShowConstraintMulti.
    def exitShowConstraintMulti(self, ctx:Cypher5Parser.ShowConstraintMultiContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#ShowConstraintUnique.
    def enterShowConstraintUnique(self, ctx:Cypher5Parser.ShowConstraintUniqueContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#ShowConstraintUnique.
    def exitShowConstraintUnique(self, ctx:Cypher5Parser.ShowConstraintUniqueContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#ShowConstraintKey.
    def enterShowConstraintKey(self, ctx:Cypher5Parser.ShowConstraintKeyContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#ShowConstraintKey.
    def exitShowConstraintKey(self, ctx:Cypher5Parser.ShowConstraintKeyContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#ShowConstraintRelExist.
    def enterShowConstraintRelExist(self, ctx:Cypher5Parser.ShowConstraintRelExistContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#ShowConstraintRelExist.
    def exitShowConstraintRelExist(self, ctx:Cypher5Parser.ShowConstraintRelExistContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#ShowConstraintOldExists.
    def enterShowConstraintOldExists(self, ctx:Cypher5Parser.ShowConstraintOldExistsContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#ShowConstraintOldExists.
    def exitShowConstraintOldExists(self, ctx:Cypher5Parser.ShowConstraintOldExistsContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#ShowConstraintBriefAndYield.
    def enterShowConstraintBriefAndYield(self, ctx:Cypher5Parser.ShowConstraintBriefAndYieldContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#ShowConstraintBriefAndYield.
    def exitShowConstraintBriefAndYield(self, ctx:Cypher5Parser.ShowConstraintBriefAndYieldContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#constraintAllowYieldType.
    def enterConstraintAllowYieldType(self, ctx:Cypher5Parser.ConstraintAllowYieldTypeContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#constraintAllowYieldType.
    def exitConstraintAllowYieldType(self, ctx:Cypher5Parser.ConstraintAllowYieldTypeContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#constraintExistType.
    def enterConstraintExistType(self, ctx:Cypher5Parser.ConstraintExistTypeContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#constraintExistType.
    def exitConstraintExistType(self, ctx:Cypher5Parser.ConstraintExistTypeContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#constraintBriefAndYieldType.
    def enterConstraintBriefAndYieldType(self, ctx:Cypher5Parser.ConstraintBriefAndYieldTypeContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#constraintBriefAndYieldType.
    def exitConstraintBriefAndYieldType(self, ctx:Cypher5Parser.ConstraintBriefAndYieldTypeContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#showConstraintsAllowBriefAndYield.
    def enterShowConstraintsAllowBriefAndYield(self, ctx:Cypher5Parser.ShowConstraintsAllowBriefAndYieldContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#showConstraintsAllowBriefAndYield.
    def exitShowConstraintsAllowBriefAndYield(self, ctx:Cypher5Parser.ShowConstraintsAllowBriefAndYieldContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#showConstraintsAllowBrief.
    def enterShowConstraintsAllowBrief(self, ctx:Cypher5Parser.ShowConstraintsAllowBriefContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#showConstraintsAllowBrief.
    def exitShowConstraintsAllowBrief(self, ctx:Cypher5Parser.ShowConstraintsAllowBriefContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#showConstraintsAllowYield.
    def enterShowConstraintsAllowYield(self, ctx:Cypher5Parser.ShowConstraintsAllowYieldContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#showConstraintsAllowYield.
    def exitShowConstraintsAllowYield(self, ctx:Cypher5Parser.ShowConstraintsAllowYieldContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#showProcedures.
    def enterShowProcedures(self, ctx:Cypher5Parser.ShowProceduresContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#showProcedures.
    def exitShowProcedures(self, ctx:Cypher5Parser.ShowProceduresContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#showFunctions.
    def enterShowFunctions(self, ctx:Cypher5Parser.ShowFunctionsContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#showFunctions.
    def exitShowFunctions(self, ctx:Cypher5Parser.ShowFunctionsContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#functionToken.
    def enterFunctionToken(self, ctx:Cypher5Parser.FunctionTokenContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#functionToken.
    def exitFunctionToken(self, ctx:Cypher5Parser.FunctionTokenContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#executableBy.
    def enterExecutableBy(self, ctx:Cypher5Parser.ExecutableByContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#executableBy.
    def exitExecutableBy(self, ctx:Cypher5Parser.ExecutableByContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#showFunctionsType.
    def enterShowFunctionsType(self, ctx:Cypher5Parser.ShowFunctionsTypeContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#showFunctionsType.
    def exitShowFunctionsType(self, ctx:Cypher5Parser.ShowFunctionsTypeContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#showTransactions.
    def enterShowTransactions(self, ctx:Cypher5Parser.ShowTransactionsContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#showTransactions.
    def exitShowTransactions(self, ctx:Cypher5Parser.ShowTransactionsContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#terminateTransactions.
    def enterTerminateTransactions(self, ctx:Cypher5Parser.TerminateTransactionsContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#terminateTransactions.
    def exitTerminateTransactions(self, ctx:Cypher5Parser.TerminateTransactionsContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#showSettings.
    def enterShowSettings(self, ctx:Cypher5Parser.ShowSettingsContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#showSettings.
    def exitShowSettings(self, ctx:Cypher5Parser.ShowSettingsContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#settingToken.
    def enterSettingToken(self, ctx:Cypher5Parser.SettingTokenContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#settingToken.
    def exitSettingToken(self, ctx:Cypher5Parser.SettingTokenContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#namesAndClauses.
    def enterNamesAndClauses(self, ctx:Cypher5Parser.NamesAndClausesContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#namesAndClauses.
    def exitNamesAndClauses(self, ctx:Cypher5Parser.NamesAndClausesContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#stringsOrExpression.
    def enterStringsOrExpression(self, ctx:Cypher5Parser.StringsOrExpressionContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#stringsOrExpression.
    def exitStringsOrExpression(self, ctx:Cypher5Parser.StringsOrExpressionContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#commandNodePattern.
    def enterCommandNodePattern(self, ctx:Cypher5Parser.CommandNodePatternContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#commandNodePattern.
    def exitCommandNodePattern(self, ctx:Cypher5Parser.CommandNodePatternContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#commandRelPattern.
    def enterCommandRelPattern(self, ctx:Cypher5Parser.CommandRelPatternContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#commandRelPattern.
    def exitCommandRelPattern(self, ctx:Cypher5Parser.CommandRelPatternContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#createConstraint.
    def enterCreateConstraint(self, ctx:Cypher5Parser.CreateConstraintContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#createConstraint.
    def exitCreateConstraint(self, ctx:Cypher5Parser.CreateConstraintContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#ConstraintExists.
    def enterConstraintExists(self, ctx:Cypher5Parser.ConstraintExistsContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#ConstraintExists.
    def exitConstraintExists(self, ctx:Cypher5Parser.ConstraintExistsContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#ConstraintTyped.
    def enterConstraintTyped(self, ctx:Cypher5Parser.ConstraintTypedContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#ConstraintTyped.
    def exitConstraintTyped(self, ctx:Cypher5Parser.ConstraintTypedContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#ConstraintIsUnique.
    def enterConstraintIsUnique(self, ctx:Cypher5Parser.ConstraintIsUniqueContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#ConstraintIsUnique.
    def exitConstraintIsUnique(self, ctx:Cypher5Parser.ConstraintIsUniqueContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#ConstraintKey.
    def enterConstraintKey(self, ctx:Cypher5Parser.ConstraintKeyContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#ConstraintKey.
    def exitConstraintKey(self, ctx:Cypher5Parser.ConstraintKeyContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#ConstraintIsNotNull.
    def enterConstraintIsNotNull(self, ctx:Cypher5Parser.ConstraintIsNotNullContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#ConstraintIsNotNull.
    def exitConstraintIsNotNull(self, ctx:Cypher5Parser.ConstraintIsNotNullContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#dropConstraint.
    def enterDropConstraint(self, ctx:Cypher5Parser.DropConstraintContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#dropConstraint.
    def exitDropConstraint(self, ctx:Cypher5Parser.DropConstraintContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#createIndex.
    def enterCreateIndex(self, ctx:Cypher5Parser.CreateIndexContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#createIndex.
    def exitCreateIndex(self, ctx:Cypher5Parser.CreateIndexContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#oldCreateIndex.
    def enterOldCreateIndex(self, ctx:Cypher5Parser.OldCreateIndexContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#oldCreateIndex.
    def exitOldCreateIndex(self, ctx:Cypher5Parser.OldCreateIndexContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#createIndex_.
    def enterCreateIndex_(self, ctx:Cypher5Parser.CreateIndex_Context):
        pass

    # Exit a parse tree produced by Cypher5Parser#createIndex_.
    def exitCreateIndex_(self, ctx:Cypher5Parser.CreateIndex_Context):
        pass


    # Enter a parse tree produced by Cypher5Parser#createFulltextIndex.
    def enterCreateFulltextIndex(self, ctx:Cypher5Parser.CreateFulltextIndexContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#createFulltextIndex.
    def exitCreateFulltextIndex(self, ctx:Cypher5Parser.CreateFulltextIndexContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#fulltextNodePattern.
    def enterFulltextNodePattern(self, ctx:Cypher5Parser.FulltextNodePatternContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#fulltextNodePattern.
    def exitFulltextNodePattern(self, ctx:Cypher5Parser.FulltextNodePatternContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#fulltextRelPattern.
    def enterFulltextRelPattern(self, ctx:Cypher5Parser.FulltextRelPatternContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#fulltextRelPattern.
    def exitFulltextRelPattern(self, ctx:Cypher5Parser.FulltextRelPatternContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#createLookupIndex.
    def enterCreateLookupIndex(self, ctx:Cypher5Parser.CreateLookupIndexContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#createLookupIndex.
    def exitCreateLookupIndex(self, ctx:Cypher5Parser.CreateLookupIndexContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#lookupIndexNodePattern.
    def enterLookupIndexNodePattern(self, ctx:Cypher5Parser.LookupIndexNodePatternContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#lookupIndexNodePattern.
    def exitLookupIndexNodePattern(self, ctx:Cypher5Parser.LookupIndexNodePatternContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#lookupIndexRelPattern.
    def enterLookupIndexRelPattern(self, ctx:Cypher5Parser.LookupIndexRelPatternContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#lookupIndexRelPattern.
    def exitLookupIndexRelPattern(self, ctx:Cypher5Parser.LookupIndexRelPatternContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#dropIndex.
    def enterDropIndex(self, ctx:Cypher5Parser.DropIndexContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#dropIndex.
    def exitDropIndex(self, ctx:Cypher5Parser.DropIndexContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#propertyList.
    def enterPropertyList(self, ctx:Cypher5Parser.PropertyListContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#propertyList.
    def exitPropertyList(self, ctx:Cypher5Parser.PropertyListContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#enclosedPropertyList.
    def enterEnclosedPropertyList(self, ctx:Cypher5Parser.EnclosedPropertyListContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#enclosedPropertyList.
    def exitEnclosedPropertyList(self, ctx:Cypher5Parser.EnclosedPropertyListContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#alterCommand.
    def enterAlterCommand(self, ctx:Cypher5Parser.AlterCommandContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#alterCommand.
    def exitAlterCommand(self, ctx:Cypher5Parser.AlterCommandContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#renameCommand.
    def enterRenameCommand(self, ctx:Cypher5Parser.RenameCommandContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#renameCommand.
    def exitRenameCommand(self, ctx:Cypher5Parser.RenameCommandContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#grantCommand.
    def enterGrantCommand(self, ctx:Cypher5Parser.GrantCommandContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#grantCommand.
    def exitGrantCommand(self, ctx:Cypher5Parser.GrantCommandContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#denyCommand.
    def enterDenyCommand(self, ctx:Cypher5Parser.DenyCommandContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#denyCommand.
    def exitDenyCommand(self, ctx:Cypher5Parser.DenyCommandContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#revokeCommand.
    def enterRevokeCommand(self, ctx:Cypher5Parser.RevokeCommandContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#revokeCommand.
    def exitRevokeCommand(self, ctx:Cypher5Parser.RevokeCommandContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#userNames.
    def enterUserNames(self, ctx:Cypher5Parser.UserNamesContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#userNames.
    def exitUserNames(self, ctx:Cypher5Parser.UserNamesContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#roleNames.
    def enterRoleNames(self, ctx:Cypher5Parser.RoleNamesContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#roleNames.
    def exitRoleNames(self, ctx:Cypher5Parser.RoleNamesContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#roleToken.
    def enterRoleToken(self, ctx:Cypher5Parser.RoleTokenContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#roleToken.
    def exitRoleToken(self, ctx:Cypher5Parser.RoleTokenContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#enableServerCommand.
    def enterEnableServerCommand(self, ctx:Cypher5Parser.EnableServerCommandContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#enableServerCommand.
    def exitEnableServerCommand(self, ctx:Cypher5Parser.EnableServerCommandContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#alterServer.
    def enterAlterServer(self, ctx:Cypher5Parser.AlterServerContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#alterServer.
    def exitAlterServer(self, ctx:Cypher5Parser.AlterServerContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#renameServer.
    def enterRenameServer(self, ctx:Cypher5Parser.RenameServerContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#renameServer.
    def exitRenameServer(self, ctx:Cypher5Parser.RenameServerContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#dropServer.
    def enterDropServer(self, ctx:Cypher5Parser.DropServerContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#dropServer.
    def exitDropServer(self, ctx:Cypher5Parser.DropServerContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#showServers.
    def enterShowServers(self, ctx:Cypher5Parser.ShowServersContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#showServers.
    def exitShowServers(self, ctx:Cypher5Parser.ShowServersContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#allocationCommand.
    def enterAllocationCommand(self, ctx:Cypher5Parser.AllocationCommandContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#allocationCommand.
    def exitAllocationCommand(self, ctx:Cypher5Parser.AllocationCommandContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#deallocateDatabaseFromServers.
    def enterDeallocateDatabaseFromServers(self, ctx:Cypher5Parser.DeallocateDatabaseFromServersContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#deallocateDatabaseFromServers.
    def exitDeallocateDatabaseFromServers(self, ctx:Cypher5Parser.DeallocateDatabaseFromServersContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#reallocateDatabases.
    def enterReallocateDatabases(self, ctx:Cypher5Parser.ReallocateDatabasesContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#reallocateDatabases.
    def exitReallocateDatabases(self, ctx:Cypher5Parser.ReallocateDatabasesContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#createRole.
    def enterCreateRole(self, ctx:Cypher5Parser.CreateRoleContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#createRole.
    def exitCreateRole(self, ctx:Cypher5Parser.CreateRoleContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#dropRole.
    def enterDropRole(self, ctx:Cypher5Parser.DropRoleContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#dropRole.
    def exitDropRole(self, ctx:Cypher5Parser.DropRoleContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#renameRole.
    def enterRenameRole(self, ctx:Cypher5Parser.RenameRoleContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#renameRole.
    def exitRenameRole(self, ctx:Cypher5Parser.RenameRoleContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#showRoles.
    def enterShowRoles(self, ctx:Cypher5Parser.ShowRolesContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#showRoles.
    def exitShowRoles(self, ctx:Cypher5Parser.ShowRolesContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#grantRole.
    def enterGrantRole(self, ctx:Cypher5Parser.GrantRoleContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#grantRole.
    def exitGrantRole(self, ctx:Cypher5Parser.GrantRoleContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#revokeRole.
    def enterRevokeRole(self, ctx:Cypher5Parser.RevokeRoleContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#revokeRole.
    def exitRevokeRole(self, ctx:Cypher5Parser.RevokeRoleContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#createUser.
    def enterCreateUser(self, ctx:Cypher5Parser.CreateUserContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#createUser.
    def exitCreateUser(self, ctx:Cypher5Parser.CreateUserContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#dropUser.
    def enterDropUser(self, ctx:Cypher5Parser.DropUserContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#dropUser.
    def exitDropUser(self, ctx:Cypher5Parser.DropUserContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#renameUser.
    def enterRenameUser(self, ctx:Cypher5Parser.RenameUserContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#renameUser.
    def exitRenameUser(self, ctx:Cypher5Parser.RenameUserContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#alterCurrentUser.
    def enterAlterCurrentUser(self, ctx:Cypher5Parser.AlterCurrentUserContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#alterCurrentUser.
    def exitAlterCurrentUser(self, ctx:Cypher5Parser.AlterCurrentUserContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#alterUser.
    def enterAlterUser(self, ctx:Cypher5Parser.AlterUserContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#alterUser.
    def exitAlterUser(self, ctx:Cypher5Parser.AlterUserContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#removeNamedProvider.
    def enterRemoveNamedProvider(self, ctx:Cypher5Parser.RemoveNamedProviderContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#removeNamedProvider.
    def exitRemoveNamedProvider(self, ctx:Cypher5Parser.RemoveNamedProviderContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#password.
    def enterPassword(self, ctx:Cypher5Parser.PasswordContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#password.
    def exitPassword(self, ctx:Cypher5Parser.PasswordContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#passwordOnly.
    def enterPasswordOnly(self, ctx:Cypher5Parser.PasswordOnlyContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#passwordOnly.
    def exitPasswordOnly(self, ctx:Cypher5Parser.PasswordOnlyContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#passwordExpression.
    def enterPasswordExpression(self, ctx:Cypher5Parser.PasswordExpressionContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#passwordExpression.
    def exitPasswordExpression(self, ctx:Cypher5Parser.PasswordExpressionContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#passwordChangeRequired.
    def enterPasswordChangeRequired(self, ctx:Cypher5Parser.PasswordChangeRequiredContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#passwordChangeRequired.
    def exitPasswordChangeRequired(self, ctx:Cypher5Parser.PasswordChangeRequiredContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#userStatus.
    def enterUserStatus(self, ctx:Cypher5Parser.UserStatusContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#userStatus.
    def exitUserStatus(self, ctx:Cypher5Parser.UserStatusContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#homeDatabase.
    def enterHomeDatabase(self, ctx:Cypher5Parser.HomeDatabaseContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#homeDatabase.
    def exitHomeDatabase(self, ctx:Cypher5Parser.HomeDatabaseContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#setAuthClause.
    def enterSetAuthClause(self, ctx:Cypher5Parser.SetAuthClauseContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#setAuthClause.
    def exitSetAuthClause(self, ctx:Cypher5Parser.SetAuthClauseContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#userAuthAttribute.
    def enterUserAuthAttribute(self, ctx:Cypher5Parser.UserAuthAttributeContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#userAuthAttribute.
    def exitUserAuthAttribute(self, ctx:Cypher5Parser.UserAuthAttributeContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#showUsers.
    def enterShowUsers(self, ctx:Cypher5Parser.ShowUsersContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#showUsers.
    def exitShowUsers(self, ctx:Cypher5Parser.ShowUsersContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#showCurrentUser.
    def enterShowCurrentUser(self, ctx:Cypher5Parser.ShowCurrentUserContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#showCurrentUser.
    def exitShowCurrentUser(self, ctx:Cypher5Parser.ShowCurrentUserContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#showSupportedPrivileges.
    def enterShowSupportedPrivileges(self, ctx:Cypher5Parser.ShowSupportedPrivilegesContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#showSupportedPrivileges.
    def exitShowSupportedPrivileges(self, ctx:Cypher5Parser.ShowSupportedPrivilegesContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#showPrivileges.
    def enterShowPrivileges(self, ctx:Cypher5Parser.ShowPrivilegesContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#showPrivileges.
    def exitShowPrivileges(self, ctx:Cypher5Parser.ShowPrivilegesContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#showRolePrivileges.
    def enterShowRolePrivileges(self, ctx:Cypher5Parser.ShowRolePrivilegesContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#showRolePrivileges.
    def exitShowRolePrivileges(self, ctx:Cypher5Parser.ShowRolePrivilegesContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#showUserPrivileges.
    def enterShowUserPrivileges(self, ctx:Cypher5Parser.ShowUserPrivilegesContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#showUserPrivileges.
    def exitShowUserPrivileges(self, ctx:Cypher5Parser.ShowUserPrivilegesContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#privilegeAsCommand.
    def enterPrivilegeAsCommand(self, ctx:Cypher5Parser.PrivilegeAsCommandContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#privilegeAsCommand.
    def exitPrivilegeAsCommand(self, ctx:Cypher5Parser.PrivilegeAsCommandContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#privilegeToken.
    def enterPrivilegeToken(self, ctx:Cypher5Parser.PrivilegeTokenContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#privilegeToken.
    def exitPrivilegeToken(self, ctx:Cypher5Parser.PrivilegeTokenContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#privilege.
    def enterPrivilege(self, ctx:Cypher5Parser.PrivilegeContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#privilege.
    def exitPrivilege(self, ctx:Cypher5Parser.PrivilegeContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#allPrivilege.
    def enterAllPrivilege(self, ctx:Cypher5Parser.AllPrivilegeContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#allPrivilege.
    def exitAllPrivilege(self, ctx:Cypher5Parser.AllPrivilegeContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#allPrivilegeType.
    def enterAllPrivilegeType(self, ctx:Cypher5Parser.AllPrivilegeTypeContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#allPrivilegeType.
    def exitAllPrivilegeType(self, ctx:Cypher5Parser.AllPrivilegeTypeContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#DefaultTarget.
    def enterDefaultTarget(self, ctx:Cypher5Parser.DefaultTargetContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#DefaultTarget.
    def exitDefaultTarget(self, ctx:Cypher5Parser.DefaultTargetContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#DatabaseVariableTarget.
    def enterDatabaseVariableTarget(self, ctx:Cypher5Parser.DatabaseVariableTargetContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#DatabaseVariableTarget.
    def exitDatabaseVariableTarget(self, ctx:Cypher5Parser.DatabaseVariableTargetContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#GraphVariableTarget.
    def enterGraphVariableTarget(self, ctx:Cypher5Parser.GraphVariableTargetContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#GraphVariableTarget.
    def exitGraphVariableTarget(self, ctx:Cypher5Parser.GraphVariableTargetContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#DBMSTarget.
    def enterDBMSTarget(self, ctx:Cypher5Parser.DBMSTargetContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#DBMSTarget.
    def exitDBMSTarget(self, ctx:Cypher5Parser.DBMSTargetContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#createPrivilege.
    def enterCreatePrivilege(self, ctx:Cypher5Parser.CreatePrivilegeContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#createPrivilege.
    def exitCreatePrivilege(self, ctx:Cypher5Parser.CreatePrivilegeContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#createPrivilegeForDatabase.
    def enterCreatePrivilegeForDatabase(self, ctx:Cypher5Parser.CreatePrivilegeForDatabaseContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#createPrivilegeForDatabase.
    def exitCreatePrivilegeForDatabase(self, ctx:Cypher5Parser.CreatePrivilegeForDatabaseContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#createNodePrivilegeToken.
    def enterCreateNodePrivilegeToken(self, ctx:Cypher5Parser.CreateNodePrivilegeTokenContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#createNodePrivilegeToken.
    def exitCreateNodePrivilegeToken(self, ctx:Cypher5Parser.CreateNodePrivilegeTokenContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#createRelPrivilegeToken.
    def enterCreateRelPrivilegeToken(self, ctx:Cypher5Parser.CreateRelPrivilegeTokenContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#createRelPrivilegeToken.
    def exitCreateRelPrivilegeToken(self, ctx:Cypher5Parser.CreateRelPrivilegeTokenContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#createPropertyPrivilegeToken.
    def enterCreatePropertyPrivilegeToken(self, ctx:Cypher5Parser.CreatePropertyPrivilegeTokenContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#createPropertyPrivilegeToken.
    def exitCreatePropertyPrivilegeToken(self, ctx:Cypher5Parser.CreatePropertyPrivilegeTokenContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#actionForDBMS.
    def enterActionForDBMS(self, ctx:Cypher5Parser.ActionForDBMSContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#actionForDBMS.
    def exitActionForDBMS(self, ctx:Cypher5Parser.ActionForDBMSContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#dropPrivilege.
    def enterDropPrivilege(self, ctx:Cypher5Parser.DropPrivilegeContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#dropPrivilege.
    def exitDropPrivilege(self, ctx:Cypher5Parser.DropPrivilegeContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#loadPrivilege.
    def enterLoadPrivilege(self, ctx:Cypher5Parser.LoadPrivilegeContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#loadPrivilege.
    def exitLoadPrivilege(self, ctx:Cypher5Parser.LoadPrivilegeContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#showPrivilege.
    def enterShowPrivilege(self, ctx:Cypher5Parser.ShowPrivilegeContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#showPrivilege.
    def exitShowPrivilege(self, ctx:Cypher5Parser.ShowPrivilegeContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#setPrivilege.
    def enterSetPrivilege(self, ctx:Cypher5Parser.SetPrivilegeContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#setPrivilege.
    def exitSetPrivilege(self, ctx:Cypher5Parser.SetPrivilegeContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#passwordToken.
    def enterPasswordToken(self, ctx:Cypher5Parser.PasswordTokenContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#passwordToken.
    def exitPasswordToken(self, ctx:Cypher5Parser.PasswordTokenContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#removePrivilege.
    def enterRemovePrivilege(self, ctx:Cypher5Parser.RemovePrivilegeContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#removePrivilege.
    def exitRemovePrivilege(self, ctx:Cypher5Parser.RemovePrivilegeContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#writePrivilege.
    def enterWritePrivilege(self, ctx:Cypher5Parser.WritePrivilegeContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#writePrivilege.
    def exitWritePrivilege(self, ctx:Cypher5Parser.WritePrivilegeContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#databasePrivilege.
    def enterDatabasePrivilege(self, ctx:Cypher5Parser.DatabasePrivilegeContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#databasePrivilege.
    def exitDatabasePrivilege(self, ctx:Cypher5Parser.DatabasePrivilegeContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#dbmsPrivilege.
    def enterDbmsPrivilege(self, ctx:Cypher5Parser.DbmsPrivilegeContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#dbmsPrivilege.
    def exitDbmsPrivilege(self, ctx:Cypher5Parser.DbmsPrivilegeContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#dbmsPrivilegeExecute.
    def enterDbmsPrivilegeExecute(self, ctx:Cypher5Parser.DbmsPrivilegeExecuteContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#dbmsPrivilegeExecute.
    def exitDbmsPrivilegeExecute(self, ctx:Cypher5Parser.DbmsPrivilegeExecuteContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#adminToken.
    def enterAdminToken(self, ctx:Cypher5Parser.AdminTokenContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#adminToken.
    def exitAdminToken(self, ctx:Cypher5Parser.AdminTokenContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#procedureToken.
    def enterProcedureToken(self, ctx:Cypher5Parser.ProcedureTokenContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#procedureToken.
    def exitProcedureToken(self, ctx:Cypher5Parser.ProcedureTokenContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#indexToken.
    def enterIndexToken(self, ctx:Cypher5Parser.IndexTokenContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#indexToken.
    def exitIndexToken(self, ctx:Cypher5Parser.IndexTokenContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#constraintToken.
    def enterConstraintToken(self, ctx:Cypher5Parser.ConstraintTokenContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#constraintToken.
    def exitConstraintToken(self, ctx:Cypher5Parser.ConstraintTokenContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#transactionToken.
    def enterTransactionToken(self, ctx:Cypher5Parser.TransactionTokenContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#transactionToken.
    def exitTransactionToken(self, ctx:Cypher5Parser.TransactionTokenContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#userQualifier.
    def enterUserQualifier(self, ctx:Cypher5Parser.UserQualifierContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#userQualifier.
    def exitUserQualifier(self, ctx:Cypher5Parser.UserQualifierContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#executeFunctionQualifier.
    def enterExecuteFunctionQualifier(self, ctx:Cypher5Parser.ExecuteFunctionQualifierContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#executeFunctionQualifier.
    def exitExecuteFunctionQualifier(self, ctx:Cypher5Parser.ExecuteFunctionQualifierContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#executeProcedureQualifier.
    def enterExecuteProcedureQualifier(self, ctx:Cypher5Parser.ExecuteProcedureQualifierContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#executeProcedureQualifier.
    def exitExecuteProcedureQualifier(self, ctx:Cypher5Parser.ExecuteProcedureQualifierContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#settingQualifier.
    def enterSettingQualifier(self, ctx:Cypher5Parser.SettingQualifierContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#settingQualifier.
    def exitSettingQualifier(self, ctx:Cypher5Parser.SettingQualifierContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#globs.
    def enterGlobs(self, ctx:Cypher5Parser.GlobsContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#globs.
    def exitGlobs(self, ctx:Cypher5Parser.GlobsContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#glob.
    def enterGlob(self, ctx:Cypher5Parser.GlobContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#glob.
    def exitGlob(self, ctx:Cypher5Parser.GlobContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#globRecursive.
    def enterGlobRecursive(self, ctx:Cypher5Parser.GlobRecursiveContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#globRecursive.
    def exitGlobRecursive(self, ctx:Cypher5Parser.GlobRecursiveContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#globPart.
    def enterGlobPart(self, ctx:Cypher5Parser.GlobPartContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#globPart.
    def exitGlobPart(self, ctx:Cypher5Parser.GlobPartContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#qualifiedGraphPrivilegesWithProperty.
    def enterQualifiedGraphPrivilegesWithProperty(self, ctx:Cypher5Parser.QualifiedGraphPrivilegesWithPropertyContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#qualifiedGraphPrivilegesWithProperty.
    def exitQualifiedGraphPrivilegesWithProperty(self, ctx:Cypher5Parser.QualifiedGraphPrivilegesWithPropertyContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#qualifiedGraphPrivileges.
    def enterQualifiedGraphPrivileges(self, ctx:Cypher5Parser.QualifiedGraphPrivilegesContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#qualifiedGraphPrivileges.
    def exitQualifiedGraphPrivileges(self, ctx:Cypher5Parser.QualifiedGraphPrivilegesContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#labelsResource.
    def enterLabelsResource(self, ctx:Cypher5Parser.LabelsResourceContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#labelsResource.
    def exitLabelsResource(self, ctx:Cypher5Parser.LabelsResourceContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#propertiesResource.
    def enterPropertiesResource(self, ctx:Cypher5Parser.PropertiesResourceContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#propertiesResource.
    def exitPropertiesResource(self, ctx:Cypher5Parser.PropertiesResourceContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#nonEmptyStringList.
    def enterNonEmptyStringList(self, ctx:Cypher5Parser.NonEmptyStringListContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#nonEmptyStringList.
    def exitNonEmptyStringList(self, ctx:Cypher5Parser.NonEmptyStringListContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#graphQualifier.
    def enterGraphQualifier(self, ctx:Cypher5Parser.GraphQualifierContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#graphQualifier.
    def exitGraphQualifier(self, ctx:Cypher5Parser.GraphQualifierContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#graphQualifierToken.
    def enterGraphQualifierToken(self, ctx:Cypher5Parser.GraphQualifierTokenContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#graphQualifierToken.
    def exitGraphQualifierToken(self, ctx:Cypher5Parser.GraphQualifierTokenContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#relToken.
    def enterRelToken(self, ctx:Cypher5Parser.RelTokenContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#relToken.
    def exitRelToken(self, ctx:Cypher5Parser.RelTokenContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#elementToken.
    def enterElementToken(self, ctx:Cypher5Parser.ElementTokenContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#elementToken.
    def exitElementToken(self, ctx:Cypher5Parser.ElementTokenContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#nodeToken.
    def enterNodeToken(self, ctx:Cypher5Parser.NodeTokenContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#nodeToken.
    def exitNodeToken(self, ctx:Cypher5Parser.NodeTokenContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#databaseScope.
    def enterDatabaseScope(self, ctx:Cypher5Parser.DatabaseScopeContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#databaseScope.
    def exitDatabaseScope(self, ctx:Cypher5Parser.DatabaseScopeContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#graphScope.
    def enterGraphScope(self, ctx:Cypher5Parser.GraphScopeContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#graphScope.
    def exitGraphScope(self, ctx:Cypher5Parser.GraphScopeContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#createCompositeDatabase.
    def enterCreateCompositeDatabase(self, ctx:Cypher5Parser.CreateCompositeDatabaseContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#createCompositeDatabase.
    def exitCreateCompositeDatabase(self, ctx:Cypher5Parser.CreateCompositeDatabaseContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#createDatabase.
    def enterCreateDatabase(self, ctx:Cypher5Parser.CreateDatabaseContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#createDatabase.
    def exitCreateDatabase(self, ctx:Cypher5Parser.CreateDatabaseContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#primaryTopology.
    def enterPrimaryTopology(self, ctx:Cypher5Parser.PrimaryTopologyContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#primaryTopology.
    def exitPrimaryTopology(self, ctx:Cypher5Parser.PrimaryTopologyContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#primaryToken.
    def enterPrimaryToken(self, ctx:Cypher5Parser.PrimaryTokenContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#primaryToken.
    def exitPrimaryToken(self, ctx:Cypher5Parser.PrimaryTokenContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#secondaryTopology.
    def enterSecondaryTopology(self, ctx:Cypher5Parser.SecondaryTopologyContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#secondaryTopology.
    def exitSecondaryTopology(self, ctx:Cypher5Parser.SecondaryTopologyContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#secondaryToken.
    def enterSecondaryToken(self, ctx:Cypher5Parser.SecondaryTokenContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#secondaryToken.
    def exitSecondaryToken(self, ctx:Cypher5Parser.SecondaryTokenContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#defaultLanguageSpecification.
    def enterDefaultLanguageSpecification(self, ctx:Cypher5Parser.DefaultLanguageSpecificationContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#defaultLanguageSpecification.
    def exitDefaultLanguageSpecification(self, ctx:Cypher5Parser.DefaultLanguageSpecificationContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#dropDatabase.
    def enterDropDatabase(self, ctx:Cypher5Parser.DropDatabaseContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#dropDatabase.
    def exitDropDatabase(self, ctx:Cypher5Parser.DropDatabaseContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#aliasAction.
    def enterAliasAction(self, ctx:Cypher5Parser.AliasActionContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#aliasAction.
    def exitAliasAction(self, ctx:Cypher5Parser.AliasActionContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#alterDatabase.
    def enterAlterDatabase(self, ctx:Cypher5Parser.AlterDatabaseContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#alterDatabase.
    def exitAlterDatabase(self, ctx:Cypher5Parser.AlterDatabaseContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#alterDatabaseAccess.
    def enterAlterDatabaseAccess(self, ctx:Cypher5Parser.AlterDatabaseAccessContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#alterDatabaseAccess.
    def exitAlterDatabaseAccess(self, ctx:Cypher5Parser.AlterDatabaseAccessContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#alterDatabaseTopology.
    def enterAlterDatabaseTopology(self, ctx:Cypher5Parser.AlterDatabaseTopologyContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#alterDatabaseTopology.
    def exitAlterDatabaseTopology(self, ctx:Cypher5Parser.AlterDatabaseTopologyContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#alterDatabaseOption.
    def enterAlterDatabaseOption(self, ctx:Cypher5Parser.AlterDatabaseOptionContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#alterDatabaseOption.
    def exitAlterDatabaseOption(self, ctx:Cypher5Parser.AlterDatabaseOptionContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#startDatabase.
    def enterStartDatabase(self, ctx:Cypher5Parser.StartDatabaseContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#startDatabase.
    def exitStartDatabase(self, ctx:Cypher5Parser.StartDatabaseContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#stopDatabase.
    def enterStopDatabase(self, ctx:Cypher5Parser.StopDatabaseContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#stopDatabase.
    def exitStopDatabase(self, ctx:Cypher5Parser.StopDatabaseContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#waitClause.
    def enterWaitClause(self, ctx:Cypher5Parser.WaitClauseContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#waitClause.
    def exitWaitClause(self, ctx:Cypher5Parser.WaitClauseContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#secondsToken.
    def enterSecondsToken(self, ctx:Cypher5Parser.SecondsTokenContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#secondsToken.
    def exitSecondsToken(self, ctx:Cypher5Parser.SecondsTokenContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#showDatabase.
    def enterShowDatabase(self, ctx:Cypher5Parser.ShowDatabaseContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#showDatabase.
    def exitShowDatabase(self, ctx:Cypher5Parser.ShowDatabaseContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#aliasName.
    def enterAliasName(self, ctx:Cypher5Parser.AliasNameContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#aliasName.
    def exitAliasName(self, ctx:Cypher5Parser.AliasNameContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#databaseName.
    def enterDatabaseName(self, ctx:Cypher5Parser.DatabaseNameContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#databaseName.
    def exitDatabaseName(self, ctx:Cypher5Parser.DatabaseNameContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#createAlias.
    def enterCreateAlias(self, ctx:Cypher5Parser.CreateAliasContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#createAlias.
    def exitCreateAlias(self, ctx:Cypher5Parser.CreateAliasContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#dropAlias.
    def enterDropAlias(self, ctx:Cypher5Parser.DropAliasContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#dropAlias.
    def exitDropAlias(self, ctx:Cypher5Parser.DropAliasContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#alterAlias.
    def enterAlterAlias(self, ctx:Cypher5Parser.AlterAliasContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#alterAlias.
    def exitAlterAlias(self, ctx:Cypher5Parser.AlterAliasContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#alterAliasTarget.
    def enterAlterAliasTarget(self, ctx:Cypher5Parser.AlterAliasTargetContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#alterAliasTarget.
    def exitAlterAliasTarget(self, ctx:Cypher5Parser.AlterAliasTargetContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#alterAliasUser.
    def enterAlterAliasUser(self, ctx:Cypher5Parser.AlterAliasUserContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#alterAliasUser.
    def exitAlterAliasUser(self, ctx:Cypher5Parser.AlterAliasUserContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#alterAliasPassword.
    def enterAlterAliasPassword(self, ctx:Cypher5Parser.AlterAliasPasswordContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#alterAliasPassword.
    def exitAlterAliasPassword(self, ctx:Cypher5Parser.AlterAliasPasswordContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#alterAliasDriver.
    def enterAlterAliasDriver(self, ctx:Cypher5Parser.AlterAliasDriverContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#alterAliasDriver.
    def exitAlterAliasDriver(self, ctx:Cypher5Parser.AlterAliasDriverContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#alterAliasProperties.
    def enterAlterAliasProperties(self, ctx:Cypher5Parser.AlterAliasPropertiesContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#alterAliasProperties.
    def exitAlterAliasProperties(self, ctx:Cypher5Parser.AlterAliasPropertiesContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#showAliases.
    def enterShowAliases(self, ctx:Cypher5Parser.ShowAliasesContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#showAliases.
    def exitShowAliases(self, ctx:Cypher5Parser.ShowAliasesContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#commandNameExpression.
    def enterCommandNameExpression(self, ctx:Cypher5Parser.CommandNameExpressionContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#commandNameExpression.
    def exitCommandNameExpression(self, ctx:Cypher5Parser.CommandNameExpressionContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#symbolicNameOrStringParameterList.
    def enterSymbolicNameOrStringParameterList(self, ctx:Cypher5Parser.SymbolicNameOrStringParameterListContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#symbolicNameOrStringParameterList.
    def exitSymbolicNameOrStringParameterList(self, ctx:Cypher5Parser.SymbolicNameOrStringParameterListContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#symbolicAliasNameList.
    def enterSymbolicAliasNameList(self, ctx:Cypher5Parser.SymbolicAliasNameListContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#symbolicAliasNameList.
    def exitSymbolicAliasNameList(self, ctx:Cypher5Parser.SymbolicAliasNameListContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#symbolicAliasNameOrParameter.
    def enterSymbolicAliasNameOrParameter(self, ctx:Cypher5Parser.SymbolicAliasNameOrParameterContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#symbolicAliasNameOrParameter.
    def exitSymbolicAliasNameOrParameter(self, ctx:Cypher5Parser.SymbolicAliasNameOrParameterContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#symbolicAliasName.
    def enterSymbolicAliasName(self, ctx:Cypher5Parser.SymbolicAliasNameContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#symbolicAliasName.
    def exitSymbolicAliasName(self, ctx:Cypher5Parser.SymbolicAliasNameContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#stringListLiteral.
    def enterStringListLiteral(self, ctx:Cypher5Parser.StringListLiteralContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#stringListLiteral.
    def exitStringListLiteral(self, ctx:Cypher5Parser.StringListLiteralContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#stringList.
    def enterStringList(self, ctx:Cypher5Parser.StringListContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#stringList.
    def exitStringList(self, ctx:Cypher5Parser.StringListContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#stringLiteral.
    def enterStringLiteral(self, ctx:Cypher5Parser.StringLiteralContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#stringLiteral.
    def exitStringLiteral(self, ctx:Cypher5Parser.StringLiteralContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#stringOrParameterExpression.
    def enterStringOrParameterExpression(self, ctx:Cypher5Parser.StringOrParameterExpressionContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#stringOrParameterExpression.
    def exitStringOrParameterExpression(self, ctx:Cypher5Parser.StringOrParameterExpressionContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#stringOrParameter.
    def enterStringOrParameter(self, ctx:Cypher5Parser.StringOrParameterContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#stringOrParameter.
    def exitStringOrParameter(self, ctx:Cypher5Parser.StringOrParameterContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#uIntOrIntParameter.
    def enterUIntOrIntParameter(self, ctx:Cypher5Parser.UIntOrIntParameterContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#uIntOrIntParameter.
    def exitUIntOrIntParameter(self, ctx:Cypher5Parser.UIntOrIntParameterContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#mapOrParameter.
    def enterMapOrParameter(self, ctx:Cypher5Parser.MapOrParameterContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#mapOrParameter.
    def exitMapOrParameter(self, ctx:Cypher5Parser.MapOrParameterContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#map.
    def enterMap(self, ctx:Cypher5Parser.MapContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#map.
    def exitMap(self, ctx:Cypher5Parser.MapContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#symbolicVariableNameString.
    def enterSymbolicVariableNameString(self, ctx:Cypher5Parser.SymbolicVariableNameStringContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#symbolicVariableNameString.
    def exitSymbolicVariableNameString(self, ctx:Cypher5Parser.SymbolicVariableNameStringContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#escapedSymbolicVariableNameString.
    def enterEscapedSymbolicVariableNameString(self, ctx:Cypher5Parser.EscapedSymbolicVariableNameStringContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#escapedSymbolicVariableNameString.
    def exitEscapedSymbolicVariableNameString(self, ctx:Cypher5Parser.EscapedSymbolicVariableNameStringContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#unescapedSymbolicVariableNameString.
    def enterUnescapedSymbolicVariableNameString(self, ctx:Cypher5Parser.UnescapedSymbolicVariableNameStringContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#unescapedSymbolicVariableNameString.
    def exitUnescapedSymbolicVariableNameString(self, ctx:Cypher5Parser.UnescapedSymbolicVariableNameStringContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#symbolicNameString.
    def enterSymbolicNameString(self, ctx:Cypher5Parser.SymbolicNameStringContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#symbolicNameString.
    def exitSymbolicNameString(self, ctx:Cypher5Parser.SymbolicNameStringContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#escapedSymbolicNameString.
    def enterEscapedSymbolicNameString(self, ctx:Cypher5Parser.EscapedSymbolicNameStringContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#escapedSymbolicNameString.
    def exitEscapedSymbolicNameString(self, ctx:Cypher5Parser.EscapedSymbolicNameStringContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#unescapedSymbolicNameString.
    def enterUnescapedSymbolicNameString(self, ctx:Cypher5Parser.UnescapedSymbolicNameStringContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#unescapedSymbolicNameString.
    def exitUnescapedSymbolicNameString(self, ctx:Cypher5Parser.UnescapedSymbolicNameStringContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#symbolicLabelNameString.
    def enterSymbolicLabelNameString(self, ctx:Cypher5Parser.SymbolicLabelNameStringContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#symbolicLabelNameString.
    def exitSymbolicLabelNameString(self, ctx:Cypher5Parser.SymbolicLabelNameStringContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#unescapedLabelSymbolicNameString.
    def enterUnescapedLabelSymbolicNameString(self, ctx:Cypher5Parser.UnescapedLabelSymbolicNameStringContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#unescapedLabelSymbolicNameString.
    def exitUnescapedLabelSymbolicNameString(self, ctx:Cypher5Parser.UnescapedLabelSymbolicNameStringContext):
        pass


    # Enter a parse tree produced by Cypher5Parser#unescapedLabelSymbolicNameString_.
    def enterUnescapedLabelSymbolicNameString_(self, ctx:Cypher5Parser.UnescapedLabelSymbolicNameString_Context):
        pass

    # Exit a parse tree produced by Cypher5Parser#unescapedLabelSymbolicNameString_.
    def exitUnescapedLabelSymbolicNameString_(self, ctx:Cypher5Parser.UnescapedLabelSymbolicNameString_Context):
        pass


    # Enter a parse tree produced by Cypher5Parser#endOfFile.
    def enterEndOfFile(self, ctx:Cypher5Parser.EndOfFileContext):
        pass

    # Exit a parse tree produced by Cypher5Parser#endOfFile.
    def exitEndOfFile(self, ctx:Cypher5Parser.EndOfFileContext):
        pass



del Cypher5Parser