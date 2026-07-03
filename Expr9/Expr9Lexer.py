# Generated from Expr9.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,7,43,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,1,0,1,0,1,0,1,1,4,1,20,8,1,11,1,12,1,21,1,2,1,2,5,2,26,8,2,
        10,2,12,2,29,9,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,4,6,38,8,6,11,6,12,
        6,39,1,6,1,6,0,0,7,1,1,3,2,5,3,7,4,9,5,11,6,13,7,1,0,4,1,0,48,57,
        3,0,65,90,95,95,97,122,4,0,48,57,65,90,95,95,97,122,3,0,9,10,13,
        13,32,32,45,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,
        1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,1,15,1,0,0,0,3,19,1,0,0,0,5,23,
        1,0,0,0,7,30,1,0,0,0,9,32,1,0,0,0,11,34,1,0,0,0,13,37,1,0,0,0,15,
        16,5,105,0,0,16,17,5,102,0,0,17,2,1,0,0,0,18,20,7,0,0,0,19,18,1,
        0,0,0,20,21,1,0,0,0,21,19,1,0,0,0,21,22,1,0,0,0,22,4,1,0,0,0,23,
        27,7,1,0,0,24,26,7,2,0,0,25,24,1,0,0,0,26,29,1,0,0,0,27,25,1,0,0,
        0,27,28,1,0,0,0,28,6,1,0,0,0,29,27,1,0,0,0,30,31,5,62,0,0,31,8,1,
        0,0,0,32,33,5,40,0,0,33,10,1,0,0,0,34,35,5,41,0,0,35,12,1,0,0,0,
        36,38,7,3,0,0,37,36,1,0,0,0,38,39,1,0,0,0,39,37,1,0,0,0,39,40,1,
        0,0,0,40,41,1,0,0,0,41,42,6,6,0,0,42,14,1,0,0,0,4,0,21,27,39,1,6,
        0,0
    ]

class Expr9Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IF = 1
    NUM = 2
    ID = 3
    MAYOR = 4
    PARENTESIS_IZQ = 5
    PARENTESIS_DER = 6
    WS = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'>'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "IF", "NUM", "ID", "MAYOR", "PARENTESIS_IZQ", "PARENTESIS_DER", 
            "WS" ]

    ruleNames = [ "IF", "NUM", "ID", "MAYOR", "PARENTESIS_IZQ", "PARENTESIS_DER", 
                  "WS" ]

    grammarFileName = "Expr9.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


