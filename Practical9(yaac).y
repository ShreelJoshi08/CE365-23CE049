%{
#include <stdio.h>
#include <stdlib.h>

void yyerror(const char *s);
int yylex();
int valid = 1;
%}

%token I T E A B INVALID_CHAR

%%

program:
    S '\n'  { if(valid) printf("Valid string\n"); }
  | S       { if(valid) printf("Valid string\n"); }
;

/* S → i E t S S' | a */
S:
    I E T S Sprime
  | A
;

/* S' → e S | ε */
Sprime:
    E S
  | /* epsilon */
;

/* E → b */
E:
    B
;

%%

void yyerror(const char *s) {
    valid = 0;
    printf("Invalid string\n");
}

int main() {
    printf("Enter the string: ");
    yyparse();
    return 0;
}