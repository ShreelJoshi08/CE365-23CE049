temp_count = 1
quadruples = []


# -------- Generate Temporary Variable --------
def new_temp():
    global temp_count
    temp = f"t{temp_count}"
    temp_count += 1
    return temp


# -------- Operator Precedence --------
def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0


# -------- Tokenizer (FIX INCLUDED) --------
def tokenize(expr):
    # FIX: handle wrong dash from Word/PDF
    expr = expr.replace('–', '-').replace('—', '-')

    tokens = []
    num = ""

    for ch in expr:
        if ch.isdigit():
            num += ch
        else:
            if num:
                tokens.append(num)
                num = ""
            if ch in "+-*/()":
                tokens.append(ch)

    if num:
        tokens.append(num)

    return tokens


# -------- Generate Quadruples --------
def generate_quadruple(expr):
    global quadruples, temp_count
    quadruples = []
    temp_count = 1

    tokens = tokenize(expr)

    values = []
    ops = []

    def apply_op():
        if len(values) < 2:
            raise Exception("Invalid")

        op = ops.pop()
        right = values.pop()
        left = values.pop()

        temp = new_temp()
        quadruples.append((op, left, right, temp))
        values.append(temp)

    i = 0
    while i < len(tokens):
        token = tokens[i]

        if token.isdigit():
            values.append(token)

        elif token == '(':
            ops.append(token)

        elif token == ')':
            while ops and ops[-1] != '(':
                apply_op()
            if not ops:
                raise Exception("Invalid")
            ops.pop()

        else:
            while (ops and ops[-1] != '(' and
                   precedence(ops[-1]) >= precedence(token)):
                apply_op()
            ops.append(token)

        i += 1

    while ops:
        if ops[-1] == '(':
            raise Exception("Invalid")
        apply_op()

    return quadruples


# -------- Print Table --------
def print_quadruples(quads):
    print("\n" + "-" * 50)
    print(f"| {'Operator':^8} | {'Operand1':^10} | {'Operand2':^10} | {'Result':^6} |")
    print("-" * 50)

    for op, op1, op2, res in quads:
        print(f"| {op:^8} | {op1:^10} | {op2:^10} | {res:^6} |")

    print("-" * 50)


# -------- MAIN --------
while True:
    expr = input("\nEnter expression (type 'exit' to stop): ")

    if expr.lower() == "exit":
        print("Program stopped.")
        break

    try:
        quads = generate_quadruple(expr)
        print_quadruples(quads)
        print("Valid expression")

    except:
        # Always print table even if invalid
        print_quadruples(quadruples)
        print("Invalid expression")