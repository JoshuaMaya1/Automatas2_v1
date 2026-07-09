from html import parser

from antlr4 import * 
from Expr7Lexer import Expr7Lexer
from Expr7Parser import Expr7Parser

entrada = input("Codigo: ")
lexer = Expr7Lexer(InputStream(entrada))
tokens = CommonTokenStream(lexer)
parser = Expr7Parser(tokens)
arbol = parser.root()


if parser.getNumberOfSyntaxErrors() == 0:
    print("Entrada correcta")
    print("Arbol de derivacion: ")
    print(arbol.toStringTree(recog=parser))
else:
    print("El codigo contiene errores de sintaxis")
    


