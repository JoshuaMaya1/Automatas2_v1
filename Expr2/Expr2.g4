grammar Expr2;

root : expr2 EOF;

expr2: EOF;

NUM : [0-9]+;
MENOS: '-';
WS : [ \t\r\n]+ -> skip;