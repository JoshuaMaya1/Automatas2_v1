grammar Expr5;

root: expr5 EOF;

expr5: PRINT CADENA;

PRINT : 'print';
CADENA : '"'~["\r\n]*'"';

WS : [ \t\r\n]+ -> skip;