%{
#include "parser.tab.h"
%}

%%

"i"     { return I; }
"t"     { return T; }
"e"     { return E; }
"a"     { return A; }
"b"     { return B; }
[ \t\n] { /* skip whitespace */ }
.       { return INVALID_CHAR; }

%%

int yywrap() {
    return 1;
}