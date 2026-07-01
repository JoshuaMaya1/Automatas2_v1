grammar Expr8;

root : expr8 EOF;

expr8: EOF;

NUM : [0-9]+;

ID : [a-zA-Z_][a-zA-Z0-9_]*;

MAYOR_IGUAL : '>=';

WS : [ \t\r\n]+ -> skip;
