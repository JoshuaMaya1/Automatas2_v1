grammar Expr7;

root : expr7 EOF;

expr7 : INT ID IGUAL NUM | INT ID expr7 IGUAL NUM expr7 | NUM | ID;

INT : 'int';
NUM : [0-9]+;
ID : [a-zA-Z_][a-zA-Z0-9_]*;
IGUAL : '=';
WS : [ \t\r\n]+ -> skip;

