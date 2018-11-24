from DataStructures.LinearDS import Stack

def checkAllPar(ipString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(ipString) and balanced:
        paranthesis = ipString[index]
        if paranthesis in "([{":
            s.push(paranthesis)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,paranthesis):
                       balanced = False
        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(par_open,par_close):
    opens = "([{"
    closers = ")]}"
    return opens.index(par_open) == closers.index(par_close)


print(checkAllPar('{{([][])}()}'))
print(checkAllPar('[{()]'))
