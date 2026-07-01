grammar Expr;

root : expr EOF;

expr: EOF;

IF : 'if';
ID : [a-zA-Z_][a-zA-Z0-9_]*;
MAYOR_QUE : '>';


NUM : [0-9]+;
MAS : '+';
WS  : [ \t\r\n]+ -> skip;