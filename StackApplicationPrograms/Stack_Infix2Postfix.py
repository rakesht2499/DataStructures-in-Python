from DataStructures.LinearDS import Stack

def infix2postfix(arr):
    opstack = Stack()
    op_list = []
    prec = {"**":4,"*":3,"/":3,"+":2,"-":2,"(":1}
    ar = arr.split(" ")
    for token in ar:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            op_list.append(token)
        elif token == "(":
            opstack.push(token)
        elif token == ")":
            top = opstack.pop()
            while top != "(":
                op_list.append(top)
                top = opstack.pop()
        else:
            while (not opstack.isEmpty()) and (prec[opstack.peek()] >= prec[token]):
                op_list.append(opstack.pop())
            opstack.push(token)

    while not opstack.isEmpty():
        op_list.append((opstack.pop()))
    return " ".join(op_list)
print(infix2postfix("5 * 3 ** ( 4 - 2 )"))
print(infix2postfix("A * B + C * D"))
print(infix2postfix("( A + B ) * C - ( D - E ) * ( F + G )"))