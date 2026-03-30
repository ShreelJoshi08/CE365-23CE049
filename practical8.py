import practical7 as first_follow

grammar = first_follow.grammar
FIRST = first_follow.FIRST
FOLLOW = first_follow.FOLLOW


# -------- Parsing Table --------
parsing_table = {}

for nt in grammar:
    parsing_table[nt] = {}


def first_of_string(symbols):
    result = set()

    for sym in symbols:

        if sym not in grammar:   # terminal
            result.add(sym)
            return result

        result |= (FIRST[sym] - {'ε'})

        if 'ε' not in FIRST[sym]:
            return result

    result.add('ε')
    return result


is_LL1 = True

for head in grammar:
    for production in grammar[head]:

        first_set = first_of_string(production)

        for terminal in first_set - {'ε'}:

            if terminal in parsing_table[head]:
                is_LL1 = False

            parsing_table[head][terminal] = production

        if 'ε' in first_set:

            for terminal in FOLLOW[head]:

                if terminal in parsing_table[head]:
                    is_LL1 = False

                parsing_table[head][terminal] = production


print("\nPredictive Parsing Table\n")

for nt in parsing_table:
    for t in parsing_table[nt]:
        print(f"M[{nt},{t}] = {nt} -> {' '.join(parsing_table[nt][t])}")


if is_LL1:
    print("\nGrammar is LL(1)")
else:
    print("\nGrammar is NOT LL(1)")
    exit()


# -------- Parser --------
def parse_string(input_string):

    stack = ['$', 'S']
    input_string = list(input_string) + ['$']

    pointer = 0

    while stack:

        top = stack.pop()
        current = input_string[pointer]

        if top == current == '$':
            return True

        # terminal
        if top not in grammar:
            if top == current:
                pointer += 1
            else:
                return False

        # non-terminal
        else:
            if current in parsing_table[top]:

                production = parsing_table[top][current]

                if production != ['ε']:
                    for sym in reversed(production):
                        stack.append(sym)

            else:
                return False

    return False



while True:
    user_input = input("\nEnter string (type 'exit' to stop): ")

    if user_input.lower() == "exit":
        print("Program stopped.")
        break

    if parse_string(user_input):
        print("Valid string")
    else:
        print("Invalid string")