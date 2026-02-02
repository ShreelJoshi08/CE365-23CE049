# FIRST and FOLLOW for given CFG (Simple & Correct)

grammar = {
    'S': [['A', 'B', 'C'], ['D']],
    'A': [['a'], ['ε']],
    'B': [['b'], ['ε']],
    'C': [['(', 'S', ')'], ['c']],
    'D': [['A', 'C']]
}

FIRST = {nt: set() for nt in grammar}
FOLLOW = {nt: set() for nt in grammar}

FOLLOW['S'].add('$')   # Start symbol


# -------- FIRST --------
def first(symbol):
    if symbol not in grammar:   # terminal
        return {symbol}

    if FIRST[symbol]:
        return FIRST[symbol]

    for prod in grammar[symbol]:
        for sym in prod:
            f = first(sym)
            FIRST[symbol] |= (f - {'ε'})
            if 'ε' not in f:
                break
        else:
            FIRST[symbol].add('ε')

    return FIRST[symbol]


for nt in grammar:
    first(nt)


# -------- FOLLOW --------
changed = True
while changed:
    changed = False
    for head in grammar:
        for prod in grammar[head]:
            for i in range(len(prod)):
                curr = prod[i]

                if curr in grammar:
                    if i + 1 < len(prod):
                        next_sym = prod[i + 1]

                        # FIX: check terminal / non-terminal
                        if next_sym in grammar:
                            FOLLOW[curr] |= (FIRST[next_sym] - {'ε'})
                        else:
                            FOLLOW[curr].add(next_sym)

                    else:
                        FOLLOW[curr] |= FOLLOW[head]



print("FIRST Sets:")
for nt in FIRST:
    print(f"First({nt}) = {FIRST[nt]}")

print("\nFOLLOW Sets:")
for nt in FOLLOW:
    print(f"Follow({nt}) = {FOLLOW[nt]}")
