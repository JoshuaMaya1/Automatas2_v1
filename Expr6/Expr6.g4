grammar Expr6;

root : expr6 EOF;

expr6: EOF;

NUM : [0-9]+;
POR : '*';
MAS : '+';
WS : [ \t\r\n]+ -> skip;