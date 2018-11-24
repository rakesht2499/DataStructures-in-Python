from DataStructures.LinearDS import Node

class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self,value):
        if self.front == None and self.rear == None:
            self.front = Node(value)
            self.rear = self.front
        else:
            self.rear.setNext(Node(value))
            self.rear = self.rear.getNext()

    def dequeue(self):
        if self.front == None:
            print("The Queue is Empty")
        else:
            self.front = self.front.getNext()
            if self.front == None:
                self.rear = None

    def isEmpty(self):
        return self.front == None

    def size(self):
        curr,count = self.front,0
        while curr != None:
            count += 1
            curr = curr.getNext()
        return count

    def __str__(self):
        curr,string = self.front,""
        while curr != None:
            string += str(curr.getData()) + " "
            curr = curr.getNext()
        return string

if __name__ == "__main__":
    print("\n --------------- Implementation of an Linked Queue --------------- \n")
    newQueue = LinkedQueue()
    print("Queue is Empty : ", newQueue.isEmpty())
    newQueue.enqueue(1)
    newQueue.enqueue(2)
    newQueue.enqueue(3)
    newQueue.enqueue(4)
    print(newQueue)
    newQueue.dequeue()
    print(newQueue)
    print("Size : ",newQueue.size())
    print("Queue is Empty : ",newQueue.isEmpty())
    newQueue.dequeue()
    newQueue.dequeue()
    newQueue.dequeue()
    newQueue.dequeue()
    print("\n --------------- END OF LINKED QUEUE --------------- \n")