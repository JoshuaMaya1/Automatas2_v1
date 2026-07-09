# Generated from Expr9.g4 by ANTLR 4.13.2
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
        4,1,7,19,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,2,1,2,1,2,0,0,3,0,2,4,0,1,1,0,2,3,15,0,6,1,0,0,0,2,9,1,
        0,0,0,4,16,1,0,0,0,6,7,3,2,1,0,7,8,5,0,0,1,8,1,1,0,0,0,9,10,5,1,
        0,0,10,11,5,5,0,0,11,12,3,4,2,0,12,13,5,4,0,0,13,14,3,4,2,0,14,15,
        5,6,0,0,15,3,1,0,0,0,16,17,7,0,0,0,17,5,1,0,0,0,0
    ]

class Expr9Parser ( Parser ):

    grammarFileName = "Expr9.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "<INVALID>", "<INVALID>", "'>'", 
                     "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "IF", "NUM", "ID", "MAYOR", "PARENTESIS_IZQ", 
                      "PARENTESIS_DER", "WS" ]

    RULE_root = 0
    RULE_expr9 = 1
    RULE_valor = 2

    ruleNames =  [ "root", "expr9", "valor" ]

    EOF = Token.EOF
    IF=1
    NUM=2
    ID=3
    MAYOR=4
    PARENTESIS_IZQ=5
    PARENTESIS_DER=6
    WS=7

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

        def expr9(self):
            return self.getTypedRuleContext(Expr9Parser.Expr9Context,0)


        def EOF(self):
            return self.getToken(Expr9Parser.EOF, 0)

        def getRuleIndex(self):
            return Expr9Parser.RULE_root




    def root(self):

        localctx = Expr9Parser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.expr9()
            self.state = 7
            self.match(Expr9Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(Expr9Parser.IF, 0)

        def PARENTESIS_IZQ(self):
            return self.getToken(Expr9Parser.PARENTESIS_IZQ, 0)

        def valor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Expr9Parser.ValorContext)
            else:
                return self.getTypedRuleContext(Expr9Parser.ValorContext,i)


        def MAYOR(self):
            return self.getToken(Expr9Parser.MAYOR, 0)

        def PARENTESIS_DER(self):
            return self.getToken(Expr9Parser.PARENTESIS_DER, 0)

        def getRuleIndex(self):
            return Expr9Parser.RULE_expr9




    def expr9(self):

        localctx = Expr9Parser.Expr9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr9)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9
            self.match(Expr9Parser.IF)
            self.state = 10
            self.match(Expr9Parser.PARENTESIS_IZQ)
            self.state = 11
            self.valor()
            self.state = 12
            self.match(Expr9Parser.MAYOR)
            self.state = 13
            self.valor()
            self.state = 14
            self.match(Expr9Parser.PARENTESIS_DER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(Expr9Parser.NUM, 0)

        def ID(self):
            return self.getToken(Expr9Parser.ID, 0)

        def getRuleIndex(self):
            return Expr9Parser.RULE_valor




    def valor(self):

        localctx = Expr9Parser.ValorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_valor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            _la = self._input.LA(1)
            if not(_la==2 or _la==3):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





