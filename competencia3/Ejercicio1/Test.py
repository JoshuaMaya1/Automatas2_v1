from html import parser

from antlr4 import * 
from Expr1Lexer import Expr1Lexer
from Expr1Parser import Expr1Parser

entrada = input("Codigo: ")
lexer = Expr1Lexer(InputStream(entrada))
tokens = CommonTokenStream(lexer)
parser = Expr1Parser(tokens)
arbol = parser.root()


if parser.getNumberOfSyntaxErrors() == 0:
    print("Entrada correcta")
    print("Arbol de derivacion: ")
    print(arbol.toStringTree(recog=parser))
else:
    print("El codigo contiene errores de sintaxis")
    


