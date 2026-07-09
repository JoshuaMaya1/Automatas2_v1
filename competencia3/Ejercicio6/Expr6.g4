grammar Expr6;

root : expr6 EOF;

expr6: expr6 POR expr6 | expr6 MAS expr6 | NUM;

NUM : [0-9]+;
POR : '*';
MAS : '+';
WS : [ \t\r\n]+ -> skip;

