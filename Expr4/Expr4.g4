grammar Expr4;

root: expr4 EOF;

expr4: EOF;

IF: 'if';
NUM: [0-9]+;

ID: [a-zA-Z_][a-zA-Z0-9_]*;

MAYOR_QUE: '>';
WS: [ \t\r\n]+ -> skip;