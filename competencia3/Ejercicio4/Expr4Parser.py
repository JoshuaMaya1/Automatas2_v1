# Generated from Expr4.g4 by ANTLR 4.13.2
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
        4,1,5,17,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        3,1,15,8,1,1,1,0,0,2,0,2,0,0,16,0,4,1,0,0,0,2,14,1,0,0,0,4,5,3,2,
        1,0,5,6,5,0,0,1,6,1,1,0,0,0,7,8,5,1,0,0,8,9,3,2,1,0,9,10,5,4,0,0,
        10,11,3,2,1,0,11,15,1,0,0,0,12,15,5,2,0,0,13,15,5,3,0,0,14,7,1,0,
        0,0,14,12,1,0,0,0,14,13,1,0,0,0,15,3,1,0,0,0,1,14
    ]

class Expr4Parser ( Parser ):

    grammarFileName = "Expr4.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "<INVALID>", "<INVALID>", "'>'" ]

    symbolicNames = [ "<INVALID>", "IF", "NUM", "ID", "MAYOR_QUE", "WS" ]

    RULE_root = 0
    RULE_expr4 = 1

    ruleNames =  [ "root", "expr4" ]

    EOF = Token.EOF
    IF=1
    NUM=2
    ID=3
    MAYOR_QUE=4
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

        def expr4(self):
            return self.getTypedRuleContext(Expr4Parser.Expr4Context,0)


        def EOF(self):
            return self.getToken(Expr4Parser.EOF, 0)

        def getRuleIndex(self):
            return Expr4Parser.RULE_root




    def root(self):

        localctx = Expr4Parser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.expr4()
            self.state = 5
            self.match(Expr4Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(Expr4Parser.IF, 0)

        def expr4(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Expr4Parser.Expr4Context)
            else:
                return self.getTypedRuleContext(Expr4Parser.Expr4Context,i)


        def MAYOR_QUE(self):
            return self.getToken(Expr4Parser.MAYOR_QUE, 0)

        def NUM(self):
            return self.getToken(Expr4Parser.NUM, 0)

        def ID(self):
            return self.getToken(Expr4Parser.ID, 0)

        def getRuleIndex(self):
            return Expr4Parser.RULE_expr4




    def expr4(self):

        localctx = Expr4Parser.Expr4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr4)
        try:
            self.state = 14
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 7
                self.match(Expr4Parser.IF)
                self.state = 8
                self.expr4()
                self.state = 9
                self.match(Expr4Parser.MAYOR_QUE)
                self.state = 10
                self.expr4()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 12
                self.match(Expr4Parser.NUM)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 13
                self.match(Expr4Parser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





