from DataStructures.LinearDS import Stack

def CheckParan(arr):
    para_s = Stack()
    balanced = True
    for x in arr:
        if x == "(":
            para_s.push(x)
        else:
            if para_s.isEmpty():
                balanced = False
                break
            else:
                para_s.pop()
    if balanced and para_s.isEmpty():
        return True
    else:
        return  False

if __name__ == '__main__':
    print(CheckParan(input("Kindly Enter the paranthesis")))