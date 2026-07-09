# Generated from Expr8.g4 by ANTLR 4.13.2
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
        4,1,4,21,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,1,1,1,1,1,3,1,11,8,1,1,1,
        1,1,1,1,5,1,16,8,1,10,1,12,1,19,9,1,1,1,0,1,2,2,0,2,0,0,20,0,4,1,
        0,0,0,2,10,1,0,0,0,4,5,3,2,1,0,5,6,5,0,0,1,6,1,1,0,0,0,7,8,6,1,-1,
        0,8,11,5,1,0,0,9,11,5,2,0,0,10,7,1,0,0,0,10,9,1,0,0,0,11,17,1,0,
        0,0,12,13,10,3,0,0,13,14,5,3,0,0,14,16,3,2,1,4,15,12,1,0,0,0,16,
        19,1,0,0,0,17,15,1,0,0,0,17,18,1,0,0,0,18,3,1,0,0,0,19,17,1,0,0,
        0,2,10,17
    ]

class Expr8Parser ( Parser ):

    grammarFileName = "Expr8.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'>='" ]

    symbolicNames = [ "<INVALID>", "NUM", "ID", "MAYOR_IGUAL", "WS" ]

    RULE_root = 0
    RULE_expr8 = 1

    ruleNames =  [ "root", "expr8" ]

    EOF = Token.EOF
    NUM=1
    ID=2
    MAYOR_IGUAL=3
    WS=4

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

        def expr8(self):
            return self.getTypedRuleContext(Expr8Parser.Expr8Context,0)


        def EOF(self):
            return self.getToken(Expr8Parser.EOF, 0)

        def getRuleIndex(self):
            return Expr8Parser.RULE_root




    def root(self):

        localctx = Expr8Parser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.expr8(0)
            self.state = 5
            self.match(Expr8Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(Expr8Parser.NUM, 0)

        def ID(self):
            return self.getToken(Expr8Parser.ID, 0)

        def expr8(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Expr8Parser.Expr8Context)
            else:
                return self.getTypedRuleContext(Expr8Parser.Expr8Context,i)


        def MAYOR_IGUAL(self):
            return self.getToken(Expr8Parser.MAYOR_IGUAL, 0)

        def getRuleIndex(self):
            return Expr8Parser.RULE_expr8



    def expr8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Expr8Parser.Expr8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.state = 8
                self.match(Expr8Parser.NUM)
                pass
            elif token in [2]:
                self.state = 9
                self.match(Expr8Parser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 17
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = Expr8Parser.Expr8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr8)
                    self.state = 12
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 13
                    self.match(Expr8Parser.MAYOR_IGUAL)
                    self.state = 14
                    self.expr8(4) 
                self.state = 19
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

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
        self._predicates[1] = self.expr8_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr8_sempred(self, localctx:Expr8Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         




