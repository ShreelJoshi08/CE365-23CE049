import math


# ---------------- Lexer ----------------
class Token:
    def __init__(self, type_, value=0):
        self.type = type_
        self.value = value


class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0

    def next_token(self):
        while self.pos < len(self.text) and self.text[self.pos].isspace():
            self.pos += 1

        if self.pos >= len(self.text):
            return Token("EOF")

        ch = self.text[self.pos]

        # Number
        if ch.isdigit() or ch == '.':
            num = ""
            while self.pos < len(self.text) and (self.text[self.pos].isdigit() or self.text[self.pos] == '.'):
                num += self.text[self.pos]
                self.pos += 1
            return Token("NUM", float(num))

        self.pos += 1

        if ch == '+':
            return Token("PLUS")
        elif ch == '-':
            return Token("MINUS")
        elif ch == '*':
            return Token("MUL")
        elif ch == '/':
            return Token("DIV")
        elif ch == '^':
            return Token("POW")
        elif ch == '(':
            return Token("LPAREN")
        elif ch == ')':
            return Token("RPAREN")

        return Token("INVALID")


# ---------------- Parser (SDD Evaluation) ----------------
class Parser:
    def __init__(self, text):
        self.lexer = Lexer(text)
        self.cur = self.lexer.next_token()

    def advance(self):
        self.cur = self.lexer.next_token()

    def expect(self, type_):
        if self.cur.type != type_:
            raise Exception("Invalid expression")
        self.advance()

    # -------- E → E + T | E - T | T --------
    def parseE(self):
        val = self.parseT()

        while self.cur.type in ("PLUS", "MINUS"):
            op = self.cur.type
            self.advance()
            tval = self.parseT()

            if op == "PLUS":
                val = val + tval
            else:
                val = val - tval

        return val

    # -------- T → T * F | T / F | F --------
    def parseT(self):
        val = self.parseF()

        while self.cur.type in ("MUL", "DIV"):
            op = self.cur.type
            self.advance()
            fval = self.parseF()

            if op == "MUL":
                val = val * fval
            else:
                if fval == 0:
                    raise Exception("Division by zero")
                val = val / fval

        return val

    # -------- F → G ^ F | G --------
    def parseF(self):
        gval = self.parseG()

        if self.cur.type == "POW":
            self.advance()
            fval = self.parseF()   # right associative
            return math.pow(gval, fval)

        return gval

    # -------- G → (E) | digit --------
    def parseG(self):
        if self.cur.type == "LPAREN":
            self.advance()
            val = self.parseE()
            self.expect("RPAREN")
            return val

        elif self.cur.type == "NUM":
            val = self.cur.value
            self.advance()
            return val

        else:
            raise Exception("Invalid expression")

    def parse(self):
        val = self.parseE()
        if self.cur.type != "EOF":
            raise Exception("Invalid expression")
        return val


# ---------------- Main ----------------
print("======================================================")
print(" Arithmetic Expression Evaluator (Bottom-Up / SDD)   ")
print("======================================================")
print("Operators: +  -  *  /  ^   Grouping: ( )")
print("Type 'exit' to quit.")
print("------------------------------------------------------")

while True:
    expr = input("\nEnter expression: ")

    if expr.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    if not expr.strip():
        continue

    try:
        parser = Parser(expr)
        result = parser.parse()

        if result == int(result):
            print("Result:", int(result))
        else:
            print("Result:", result)

    except:
        print("Invalid expression")