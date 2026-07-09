# Generated from Expr5.g4 by ANTLR 4.13.2
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
        4,1,3,11,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,0,0,2,0,2,0,
        0,8,0,4,1,0,0,0,2,7,1,0,0,0,4,5,3,2,1,0,5,6,5,0,0,1,6,1,1,0,0,0,
        7,8,5,1,0,0,8,9,5,2,0,0,9,3,1,0,0,0,0
    ]

class Expr5Parser ( Parser ):

    grammarFileName = "Expr5.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'print'" ]

    symbolicNames = [ "<INVALID>", "PRINT", "CADENA", "WS" ]

    RULE_root = 0
    RULE_expr5 = 1

    ruleNames =  [ "root", "expr5" ]

    EOF = Token.EOF
    PRINT=1
    CADENA=2
    WS=3

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

        def expr5(self):
            return self.getTypedRuleContext(Expr5Parser.Expr5Context,0)


        def EOF(self):
            return self.getToken(Expr5Parser.EOF, 0)

        def getRuleIndex(self):
            return Expr5Parser.RULE_root




    def root(self):

        localctx = Expr5Parser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.expr5()
            self.state = 5
            self.match(Expr5Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(Expr5Parser.PRINT, 0)

        def CADENA(self):
            return self.getToken(Expr5Parser.CADENA, 0)

        def getRuleIndex(self):
            return Expr5Parser.RULE_expr5




    def expr5(self):

        localctx = Expr5Parser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr5)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7
            self.match(Expr5Parser.PRINT)
            self.state = 8
            self.match(Expr5Parser.CADENA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





