grammar Expr9;

root : expr9 EOF;

expr9: EOF;

IF : 'if';
NUM : [0-9]+;

ID : [a-zA-Z_][a-zA-Z0-9_]*;

MAYOR : '>';

PARENTESIS_IZQ : '(';
PARENTESIS_DER : ')';

WS : [ \t\r\n]+ -> skip;