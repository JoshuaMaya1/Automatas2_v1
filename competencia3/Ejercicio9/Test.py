from html import parser

from antlr4 import * 
from Expr9Lexer import Expr9Lexer
from Expr9Parser import Expr9Parser

entrada = input("Codigo: ")
lexer = Expr9Lexer(InputStream(entrada))
tokens = CommonTokenStream(lexer)
parser = Expr9Parser(tokens)
arbol = parser.root()


if parser.getNumberOfSyntaxErrors() == 0:
    print("Entrada correcta")
    print("Arbol de derivacion: ")
    print(arbol.toStringTree(recog=parser))
else:
    print("El codigo contiene errores de sintaxis")
    


