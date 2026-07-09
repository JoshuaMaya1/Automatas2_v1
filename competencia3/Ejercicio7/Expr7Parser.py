# Generated from Expr7.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,5,24,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,5,1,19,8,1,10,1,12,1,22,9,1,1,1,0,1,2,2,0,2,0,0,
        22,0,4,1,0,0,0,2,7,1,0,0,0,4,5,3,2,1,0,5,6,5,0,0,1,6,1,1,0,0,0,7,
        8,6,1,-1,0,8,9,5,1,0,0,9,10,5,3,0,0,10,11,5,4,0,0,11,12,5,2,0,0,
        12,20,1,0,0,0,13,14,10,1,0,0,14,15,5,1,0,0,15,16,5,3,0,0,16,17,5,
        4,0,0,17,19,5,2,0,0,18,13,1,0,0,0,19,22,1,0,0,0,20,18,1,0,0,0,20,
        21,1,0,0,0,21,3,1,0,0,0,22,20,1,0,0,0,1,20
    ]

class Expr7Parser ( Parser ):

    grammarFileName = "Expr7.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "<INVALID>", "<INVALID>", "'='" ]

    symbolicNames = [ "<INVALID>", "INT", "NUM", "ID", "IGUAL", "WS" ]

    RULE_root = 0
    RULE_expr7 = 1

    ruleNames =  [ "root", "expr7" ]

    EOF = Token.EOF
    INT=1
    NUM=2
    ID=3
    IGUAL=4
    WS=5

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr7(self):
            return self.getTypedRuleContext(Expr7Parser.Expr7Context,0)


        def EOF(self):
            return self.getToken(Expr7Parser.EOF, 0)

        def getRuleIndex(self):
            return Expr7Parser.RULE_root




    def root(self):

        localctx = Expr7Parser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.expr7(0)
            self.state = 5
            self.match(Expr7Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(Expr7Parser.INT, 0)

        def ID(self):
            return self.getToken(Expr7Parser.ID, 0)

        def IGUAL(self):
            return self.getToken(Expr7Parser.IGUAL, 0)

        def NUM(self):
            return self.getToken(Expr7Parser.NUM, 0)

        def expr7(self):
            return self.getTypedRuleContext(Expr7Parser.Expr7Context,0)


        def getRuleIndex(self):
            return Expr7Parser.RULE_expr7



    def expr7(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Expr7Parser.Expr7Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.match(Expr7Parser.INT)
            self.state = 9
            self.match(Expr7Parser.ID)
            self.state = 10
            self.match(Expr7Parser.IGUAL)
            self.state = 11
            self.match(Expr7Parser.NUM)
            self._ctx.stop = self._input.LT(-1)
            self.state = 20
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = Expr7Parser.Expr7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr7)
                    self.state = 13
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 14
                    self.match(Expr7Parser.INT)
                    self.state = 15
                    self.match(Expr7Parser.ID)
                    self.state = 16
                    self.match(Expr7Parser.IGUAL)
                    self.state = 17
                    self.match(Expr7Parser.NUM) 
                self.state = 22
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expr7_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr7_sempred(self, localctx:Expr7Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         




