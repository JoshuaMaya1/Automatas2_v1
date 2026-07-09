# Generated from Expr7.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,5,36,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,
        0,1,0,1,1,4,1,17,8,1,11,1,12,1,18,1,2,1,2,5,2,23,8,2,10,2,12,2,26,
        9,2,1,3,1,3,1,4,4,4,31,8,4,11,4,12,4,32,1,4,1,4,0,0,5,1,1,3,2,5,
        3,7,4,9,5,1,0,4,1,0,48,57,3,0,65,90,95,95,97,122,4,0,48,57,65,90,
        95,95,97,122,3,0,9,10,13,13,32,32,38,0,1,1,0,0,0,0,3,1,0,0,0,0,5,
        1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,1,11,1,0,0,0,3,16,1,0,0,0,5,20,1,
        0,0,0,7,27,1,0,0,0,9,30,1,0,0,0,11,12,5,105,0,0,12,13,5,110,0,0,
        13,14,5,116,0,0,14,2,1,0,0,0,15,17,7,0,0,0,16,15,1,0,0,0,17,18,1,
        0,0,0,18,16,1,0,0,0,18,19,1,0,0,0,19,4,1,0,0,0,20,24,7,1,0,0,21,
        23,7,2,0,0,22,21,1,0,0,0,23,26,1,0,0,0,24,22,1,0,0,0,24,25,1,0,0,
        0,25,6,1,0,0,0,26,24,1,0,0,0,27,28,5,61,0,0,28,8,1,0,0,0,29,31,7,
        3,0,0,30,29,1,0,0,0,31,32,1,0,0,0,32,30,1,0,0,0,32,33,1,0,0,0,33,
        34,1,0,0,0,34,35,6,4,0,0,35,10,1,0,0,0,4,0,18,24,32,1,6,0,0
    ]

class Expr7Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INT = 1
    NUM = 2
    ID = 3
    IGUAL = 4
    WS = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'int'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "INT", "NUM", "ID", "IGUAL", "WS" ]

    ruleNames = [ "INT", "NUM", "ID", "IGUAL", "WS" ]

    grammarFileName = "Expr7.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


