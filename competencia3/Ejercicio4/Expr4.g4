grammar Expr4;

root: expr4 EOF;

expr4: IF expr4 MAYOR_QUE expr4 | NUM | ID;

IF: 'if';
NUM: [0-9]+;

ID: [a-zA-Z_][a-zA-Z0-9_]*;

MAYOR_QUE: '>';
WS: [ \t\r\n]+ -> skip;

