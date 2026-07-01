grammar Expr1;

root : expr1 EOF;

expr1: EOF;

NUM : [0-9]+;
MAS : '+';
WS : [ \t\r\n]+ -> skip;
