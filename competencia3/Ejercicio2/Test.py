from html import parser

from antlr4 import * 
from Expr2Lexer import Expr2Lexer
from Expr2Parser import Expr2Parser

entrada = input("Codigo: ")
lexer = Expr2Lexer(InputStream(entrada))
tokens = CommonTokenStream(lexer)
parser = Expr2Parser(tokens)
arbol = parser.root()


if parser.getNumberOfSyntaxErrors() == 0:
    print("Entrada correcta")
    print("Arbol de derivacion: ")
    print(arbol.toStringTree(recog=parser))
else:
    print("El codigo contiene errores de sintaxis")
    


