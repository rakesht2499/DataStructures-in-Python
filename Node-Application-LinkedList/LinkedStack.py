from DataStructures.LinearDS import Node

class LinkedStack:
    def __init__(self):
        self.top = None

    def push(self,value):
        if self.top == None:
            self.top = Node(value)
        else:
            temp = Node(value)
            temp.setNext(self.top)
            self.top = temp

    def pop(self):
        if self.top != None:
            self.top = self.top.getNext()
        else:
            print("Cannot perform pop() : Stack is Empty")

    def isEmpty(self):
        return self.top == None

    def size(self):
        curr,count = self.top,0
        while curr != None:
            count+=1
            curr = curr.getNext()
        return count

    def topStack(self):
        return self.top.getData()

    def __str__(self):
        curr,string = self.top,""
        while curr != None:
            string += str(curr.getData()) + " "
            curr = curr.getNext()
        return string

if __name__ == "__main__":
    print("\n --------------- Implementation of an Linked Stack --------------- \n")
    new = LinkedStack()
    print("Stack is Empty : ",new.isEmpty())
    new.push(1)
    new.push(2)
    new.push(3)
    new.push(4)
    print(new)
    new.pop()
    print(new)
    print("Size : ",new.size())
    print("Stack is Empty : ",new.isEmpty())
    print("Top of the Stack",new.topStack())
    new.pop()
    new.pop()
    new.pop()
    new.pop()
    print("\n --------------- END OF LINKED STACK --------------- \n")