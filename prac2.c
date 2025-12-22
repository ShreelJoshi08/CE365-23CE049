


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
    /*Testcases
• String over 0 and 1 where every 0 immediately followed by 11*/
    char input_string[100];
    printf("Enter input string : ");
    scanf("%s", input_string);
    int current_state = start_state;
    int length = strlen(input_string);
    for(int i = 0; i < length; i++) {
        int symbol_index;
        for(int j = 0; j < num_symbols; j++) {
            if(symbols[j] == input_string[i]) {
                symbol_index = j;
                break;
            }
        }
        current_state = transition_table[current_state][symbol_index];
    }
    int is_accepted = 0;
    for(int i = 0; i < num_accept_states; i++) {
        if(current_state == accept_states[i]) {
            is_accepted = 1;
            break;
        }
    }
    if(is_accepted) {
        printf("String accepted\n");
    } else {
        printf("String rejected\n");
    }
    
    

   
    return 0;
}