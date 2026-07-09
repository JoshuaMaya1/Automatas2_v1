from html import parser

from antlr4 import * 
from Expr5Lexer import Expr5Lexer
from Expr5Parser import Expr5Parser

entrada = input("Codigo: ")
lexer = Expr5Lexer(InputStream(entrada))
tokens = CommonTokenStream(lexer)
parser = Expr5Parser(tokens)
arbol = parser.root()


if parser.getNumberOfSyntaxErrors() == 0:
    print("Entrada correcta")
    print("Arbol de derivacion: ")
    print(arbol.toStringTree(recog=parser))
else:
    print("El codigo contiene errores de sintaxis")
    


