grammar Expr10;

root : expr10 EOF;

expr10 : EOF;

PRINT : 'print';
CADENA : '"'~["\r\n]*'"';
PARENTESIS_ABRE : '(';
PARENTESIS_CIERRA : ')';
PUNTO_COMA : ';';
WS : [ \t\r\n]+ -> skip;