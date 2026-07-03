# Generated from Expr3.g4 by ANTLR 4.13.2
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
        4,1,4,10,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,1,1,1,1,1,0,0,2,0,2,0,0,7,
        0,4,1,0,0,0,2,7,1,0,0,0,4,5,3,2,1,0,5,6,5,0,0,1,6,1,1,0,0,0,7,8,
        5,0,0,1,8,3,1,0,0,0,0
    ]

class Expr3Parser ( Parser ):

    grammarFileName = "Expr3.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'='" ]

    symbolicNames = [ "<INVALID>", "NUM", "IGUAL", "ID", "WS" ]

    RULE_root = 0
    RULE_expr3 = 1

    ruleNames =  [ "root", "expr3" ]

    EOF = Token.EOF
    NUM=1
    IGUAL=2
    ID=3
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

        def expr3(self):
            return self.getTypedRuleContext(Expr3Parser.Expr3Context,0)


        def EOF(self):
            return self.getToken(Expr3Parser.EOF, 0)

        def getRuleIndex(self):
            return Expr3Parser.RULE_root




    def root(self):

        localctx = Expr3Parser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.expr3()
            self.state = 5
            self.match(Expr3Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(Expr3Parser.EOF, 0)

        def getRuleIndex(self):
            return Expr3Parser.RULE_expr3




    def expr3(self):

        localctx = Expr3Parser.Expr3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr3)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7
            self.match(Expr3Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





