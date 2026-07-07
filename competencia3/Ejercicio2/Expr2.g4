grammar Expr2;

root : expr2 EOF;

expr2: expr2 MENOS expr2 | NUM;

NUM : [0-9]+;
MENOS: '-';
WS : [ \t\r\n]+ -> skip;