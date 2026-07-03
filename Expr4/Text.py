#Importa ANTLR4 para funciones
from antlr4 import*

from Expr6Lexer import Expr6Lexer

import sys;

#Lo que obtiene es la entrada, analiza el texto y lo separa en tokens

##archivo = sys.argv[1] if len(sys.argv) > 1 else "prueba.txt"
##input_stream = FileStream(archivo)



lexer = Expr6Lexer(InputStream(input("?")))
##lexer = Expr6Lexer(input_stream)

tokens = CommonTokenStream(lexer)
tokens.fill()

print(tokens)

for token in tokens.tokens:
    print("Texto ", token.text)
    print("Tipo de token: ", token.type)
    print("Linea", token.line)
    print("columna", token.column)
    nombre_token = lexer.symbolicNames[token.type]
    print("Tipo: ", nombre_token)

    print("---------")