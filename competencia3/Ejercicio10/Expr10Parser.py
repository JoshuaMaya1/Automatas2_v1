# Generated from Expr10.g4 by ANTLR 4.13.2
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
        4,1,6,14,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        0,0,2,0,2,0,0,11,0,4,1,0,0,0,2,7,1,0,0,0,4,5,3,2,1,0,5,6,5,0,0,1,
        6,1,1,0,0,0,7,8,5,1,0,0,8,9,5,3,0,0,9,10,5,2,0,0,10,11,5,4,0,0,11,
        12,5,5,0,0,12,3,1,0,0,0,0
    ]

class Expr10Parser ( Parser ):

    grammarFileName = "Expr10.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'print'", "<INVALID>", "'('", "')'", 
                     "';'" ]

    symbolicNames = [ "<INVALID>", "PRINT", "CADENA", "PARENTESIS_ABRE", 
                      "PARENTESIS_CIERRA", "PUNTO_COMA", "WS" ]

    RULE_root = 0
    RULE_expr10 = 1

    ruleNames =  [ "root", "expr10" ]

    EOF = Token.EOF
    PRINT=1
    CADENA=2
    PARENTESIS_ABRE=3
    PARENTESIS_CIERRA=4
    PUNTO_COMA=5
    WS=6

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

        def expr10(self):
            return self.getTypedRuleContext(Expr10Parser.Expr10Context,0)


        def EOF(self):
            return self.getToken(Expr10Parser.EOF, 0)

        def getRuleIndex(self):
            return Expr10Parser.RULE_root




    def root(self):

        localctx = Expr10Parser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.expr10()
            self.state = 5
            self.match(Expr10Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr10Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(Expr10Parser.PRINT, 0)

        def PARENTESIS_ABRE(self):
            return self.getToken(Expr10Parser.PARENTESIS_ABRE, 0)

        def CADENA(self):
            return self.getToken(Expr10Parser.CADENA, 0)

        def PARENTESIS_CIERRA(self):
            return self.getToken(Expr10Parser.PARENTESIS_CIERRA, 0)

        def PUNTO_COMA(self):
            return self.getToken(Expr10Parser.PUNTO_COMA, 0)

        def getRuleIndex(self):
            return Expr10Parser.RULE_expr10




    def expr10(self):

        localctx = Expr10Parser.Expr10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr10)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7
            self.match(Expr10Parser.PRINT)
            self.state = 8
            self.match(Expr10Parser.PARENTESIS_ABRE)
            self.state = 9
            self.match(Expr10Parser.CADENA)
            self.state = 10
            self.match(Expr10Parser.PARENTESIS_CIERRA)
            self.state = 11
            self.match(Expr10Parser.PUNTO_COMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





