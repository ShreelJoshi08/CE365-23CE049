%{
#include <stdio.h>

int characters = 0;
int words = 0;
int lines = 0;
%}

%%
\n              { lines++; characters++; }
[ \t]+          { characters += yyleng; }
[^ \t\n]+       { words++; characters += yyleng; }
.               { characters++; }
%%

int main(int argc, char *argv[])
{
    if (argc > 1)
        yyin = fopen(argv[1], "r");

    yylex();

    printf("Characters : %d\n", characters);
    printf("Words : %d\n", words);
    printf("Line : %d\n", lines);

    return 0;
}

int yywrap()
{
    return 1;
}