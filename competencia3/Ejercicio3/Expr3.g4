grammar Expr3;

root: expr3 EOF;

expr3: expr3 IGUAL expr3 | NUM | ID;

NUM: [0-9]+;
IGUAL: '=';

ID: [a-zA-Z_][a-zA-Z0-9_]*;
WS: [ \t\r\n]+ -> skip;

