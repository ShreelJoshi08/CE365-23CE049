import ast
import operator

# Supported operators
ops = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow
}


# -------- Constant Folding Function --------
def constant_fold(node):
    # If number → return value
    if isinstance(node, ast.Constant):
        return node

    # If binary operation
    if isinstance(node, ast.BinOp):
        left = constant_fold(node.left)
        right = constant_fold(node.right)

        # If both sides are constants → evaluate
        if isinstance(left, ast.Constant) and isinstance(right, ast.Constant):
            try:
                result = ops[type(node.op)](left.value, right.value)
                return ast.Constant(value=result)
            except:
                pass

        # otherwise keep expression
        node.left = left
        node.right = right
        return node

    # Variables (like x, r)
    if isinstance(node, ast.Name):
        return node

    return node


# -------- Convert AST back to string --------
def to_string(node):
    if isinstance(node, ast.Constant):
        return str(int(node.value)) if node.value == int(node.value) else str(node.value)

    if isinstance(node, ast.Name):
        return node.id

    if isinstance(node, ast.BinOp):
        left = to_string(node.left)
        right = to_string(node.right)

        op_map = {
            ast.Add: '+',
            ast.Sub: '-',
            ast.Mult: '*',
            ast.Div: '/',
            ast.Pow: '^'
        }

        op = op_map[type(node.op)]
        return f"{left} {op} {right}"

    return ""


# -------- MAIN LOOP --------
while True:
    expr = input("\nEnter expression (type 'exit' to stop): ")

    if expr.lower() == "exit":
        print("Program stopped.")
        break

    try:
        # Replace ^ with ** for Python parsing
        expr = expr.replace('^', '**')

        tree = ast.parse(expr, mode='eval')
        optimized = constant_fold(tree.body)

        result = to_string(optimized)
        print("Optimized Expression:", result)

    except:
        print("Invalid expression")