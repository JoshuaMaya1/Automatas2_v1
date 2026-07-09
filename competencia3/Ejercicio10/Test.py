from html import parser

from antlr4 import * 
from Expr10Lexer import Expr10Lexer
from Expr10Parser import Expr10Parser

entrada = input("Codigo: ")
lexer = Expr10Lexer(InputStream(entrada))
tokens = CommonTokenStream(lexer)
parser = Expr10Parser(tokens)
arbol = parser.root()


if parser.getNumberOfSyntaxErrors() == 0:
    print("Entrada correcta")
    print("Arbol de derivacion: ")
    print(arbol.toStringTree(recog=parser))
else:
    print("El codigo contiene errores de sintaxis")
    


