import string

# Keywords, operators, punctuations
keywords = {
    "int", "long", "void", "char", "return",
    "if", "else", "while", "for"
}

operators = {'+', '-', '*', '/', '=', '<', '>', '&', '%'}
punctuations = {'(', ')', '{', '}', ';', ','}


def is_number(s):
    return s.isdigit()


def lexical_analyzer(filename):
    try:
        file = open(filename, "r")
    except:
        print("Error opening file")
        return

    symbol_table = []
    lexical_errors = []

    line_no = 0
    in_block_comment = False

    print("TOKENS")

    for line in file:
        line_no += 1
        i = 0

        while i < len(line):

            # Inside block comment
            if in_block_comment:
                if i + 1 < len(line) and line[i] == '*' and line[i + 1] == '/':
                    in_block_comment = False
                    i += 2
                else:
                    i += 1
                continue

            # Start block comment
            if i + 1 < len(line) and line[i] == '/' and line[i + 1] == '*':
                in_block_comment = True
                i += 2
                continue

            # Single-line comment
            if i + 1 < len(line) and line[i] == '/' and line[i + 1] == '/':
                break

            if line[i].isspace():
                i += 1
                continue

            # Identifier or keyword
            if line[i].isalpha() or line[i] == '_':
                word = ""
                while i < len(line) and (line[i].isalnum() or line[i] == '_'):
                    word += line[i]
                    i += 1

                if word in keywords:
                    print(f"Keyword: {word}")
                else:
                    print(f"Identifier: {word}")
                    if word not in symbol_table:
                        symbol_table.append(word)
                continue

            # Numeric constant
            if line[i].isdigit():
                num = ""
                while i < len(line) and (line[i].isalnum() or line[i] == '.'):
                    num += line[i]
                    i += 1

                if is_number(num):
                    print(f"Constant: {num}")
                else:
                    lexical_errors.append(
                        f"Line {line_no} : {num} invalid lexeme"
                    )
                continue

            # String constant
            if line[i] == '"':
                s = '"'
                i += 1
                while i < len(line) and line[i] != '"':
                    s += line[i]
                    i += 1
                s += '"'
                print(f"Constant: {s}")
                i += 1
                continue

            # Operator
            if line[i] in operators:
                print(f"Operator: {line[i]}")
                i += 1
                continue

            # Punctuation
            if line[i] in punctuations:
                print(f"Punctuation: {line[i]}")
                i += 1
                continue

            i += 1

    print("\nLEXICAL ERRORS")
    for err in lexical_errors:
        print(err)

    print("\nSYMBOL TABLE ENTRIES")
    for idx, sym in enumerate(symbol_table, start=1):
        print(f"{idx}) {sym}")

    file.close()


# Run analyzer
lexical_analyzer("testcase.c")
