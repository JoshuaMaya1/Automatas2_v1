grammar Expr10;

root : expr10 EOF;

expr10 : PRINT PARENTESIS_ABRE CADENA PARENTESIS_CIERRA PUNTO_COMA;

PRINT : 'print';
CADENA : '"'~["\r\n]*'"';
PARENTESIS_ABRE : '(';
PARENTESIS_CIERRA : ')';
PUNTO_COMA : ';';
WS : [ \t\r\n]+ -> skip;
