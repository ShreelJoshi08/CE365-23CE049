/*Practical Definition
String Validation Using Finite Automata
Objective
To implement a program that validates a given string against rules defined in
terms of finite automata.
Language Constraint
The program can be implemented in any programming language
Input requirement
• Accept rules in the form of finite automata (e.g., states, transitions, start
state, accept states) as input.
• Accept a string to be validated against the provided finite automata rules.
Expected output
• If the string adheres to the rules of the finite automata, the program should
output: "Valid String".
• If the string does not adhere to the rules, the program should output:
"Invalid String".
Sample input output

Input Output

Number of input symbols : 2
Input symbols : a b
Enter number of states : 4
Initial state : 1
Number of accepting states : 1
Accepting states : 2
Transition table :
1 to a -> 2
1 to b -> 3
2 to a -> 1
2 to b -> 4
3 to a -> 4
3 to b -> 1
4 to a -> 3
4 to b -> 2
 Testcases
• String over 0 and 1 where every 0 immediately followed by 11*/

#include<stdio.h>
#include<string.h>

int main() {
    int num_symbols, num_states, start_state, num_accept_states;
    printf("Number of input symbols : ");
    scanf("%d", &num_symbols);
    char symbols[num_symbols];
    printf("Input symbols : ");
    for(int i = 0; i < num_symbols; i++) {
        scanf(" %c", &symbols[i]);
    }

    printf("Enter number of states : ");
    scanf("%d", &num_states);
    printf("Initial state : ");
    scanf("%d", &start_state);
    printf("Number of accepting states : ");
    scanf("%d", &num_accept_states);

    int accept_states[num_accept_states];
    printf("Accepting states : ");
    for(int i = 0; i < num_accept_states; i++) {
        scanf("%d", &accept_states[i]);
    }
    int transition_table[num_states + 1][num_symbols];
    printf("Transition table :\n");
    for(int i = 0; i < num_states * num_symbols; i++) {
        int from_state, to_state;
        char symbol;
        scanf("%d to %c -> %d", &from_state, &symbol, &to_state);
        int symbol_index;
        for(int j = 0; j < num_symbols; j++) {
            if(symbols[j] == symbol) {
                symbol_index = j;
                break;
            }
        }
        transition_table[from_state][symbol_index] = to_state;

    }

   
    return 0;
}