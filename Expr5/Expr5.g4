grammar Expr5;

expr5: EOF;

PRINT : 'print';
CADENA : '"'~["\r\n]*'"';

WS : [ \t\r\n]+ -> skip;