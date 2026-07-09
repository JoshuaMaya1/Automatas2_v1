grammar Expr1;

root : expr1 EOF;

expr1: expr1 MAS expr1 | NUM;


NUM : [0-9]+;
MAS : '+';
WS : [ \t\r\n]+ -> skip;

