from DataStructures.LinearDS import Stack

def EvalPostfix(arr):
    ar_exp = arr.split(" ")
    opstack = Stack()
    for x in ar_exp:
        if x in "0123456789":
            opstack.push(int(x))
        else:
            op1 = opstack.pop()
            op2 = opstack.pop()
            result = do_math(x,op2,op1)
            opstack.push(result)
        # opstack.print_items()
    return opstack.pop()

def do_math(op,op1,op2):
    if op == "*":
        return op1 * op2
    elif op == "**":
        return op1 ** op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

if __name__ == "__main__":
    print(EvalPostfix("7 8 + 3 2 + /"))
    print(EvalPostfix("5 3 4 2 - ** *"))