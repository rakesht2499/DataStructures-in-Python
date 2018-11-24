class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self,add_item):
        self.items.append(add_item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def print_items(self):
        print("The items present in the Stack are: ")
        for x in self.items:
            print(x)

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self,add_item):
        self.items.insert(0,add_item)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def print_items(self):
        print("The items present in the Queue are: ")
        for x in self.items:
            print(x)

    def __str__(self):
        return " ".join(list(map(str,self.items)))

class Dequeue:
    def __init__(self):
        self.items = []

    def addFront(self,add_item):
        self.items.append(add_item)

    def addRear(self, add_item):
        self.items.insert(0,add_item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

    def setData(self,value):
        self.data = value

    def setNext(self,value):
        self.next = value

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

class DoubleNode:
    def __init__(self,value):
        self.data = value
        self.next = None
        self.prev = None

    def setData(self,value):
        self.data = value

    def setNext(self,value):
        self.next = value

    def setPrev(self,value):
        self.prev  = value

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def getPrev(self):
        return self.prev