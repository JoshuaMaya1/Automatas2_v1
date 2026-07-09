from html import parser

from antlr4 import * 
from Expr8Lexer import Expr8Lexer
from Expr8Parser import Expr8Parser

entrada = input("Codigo: ")
lexer = Expr8Lexer(InputStream(entrada))
tokens = CommonTokenStream(lexer)
parser = Expr8Parser(tokens)
arbol = parser.root()


if parser.getNumberOfSyntaxErrors() == 0:
    print("Entrada correcta")
    print("Arbol de derivacion: ")
    print(arbol.toStringTree(recog=parser))
else:
    print("El codigo contiene errores de sintaxis")
    


