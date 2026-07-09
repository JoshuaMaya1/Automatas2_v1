from html import parser

from antlr4 import * 
from Expr4Lexer import Expr4Lexer
from Expr4Parser import Expr4Parser

entrada = input("Codigo: ")
lexer = Expr4Lexer(InputStream(entrada))
tokens = CommonTokenStream(lexer)
parser = Expr4Parser(tokens)
arbol = parser.root()


if parser.getNumberOfSyntaxErrors() == 0:
    print("Entrada correcta")
    print("Arbol de derivacion: ")
    print(arbol.toStringTree(recog=parser))
else:
    print("El codigo contiene errores de sintaxis")
    


