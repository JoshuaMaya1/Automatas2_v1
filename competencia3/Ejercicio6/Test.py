from html import parser

from antlr4 import * 
from Expr6Lexer import Expr6Lexer
from Expr6Parser import Expr6Parser

entrada = input("Codigo: ")
lexer = Expr6Lexer(InputStream(entrada))
tokens = CommonTokenStream(lexer)
parser = Expr6Parser(tokens)
arbol = parser.root()


if parser.getNumberOfSyntaxErrors() == 0:
    print("Entrada correcta")
    print("Arbol de derivacion: ")
    print(arbol.toStringTree(recog=parser))
else:
    print("El codigo contiene errores de sintaxis")
    


