from DataStructures.LinearDS import Node

class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,newvalue):
        temp = Node(newvalue)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        curr = self.head
        count = 0
        while not curr == None:
            count += 1
            curr = curr.getNext()
        return count

    def search(self,value):
        curr = self.head
        while not curr == None:
            if curr.getData() == value:
                return True
            curr = curr.getNext()
        return False

    def remove(self,value):
        removed = "Item Not Found"
        if self.head.getData() == value:
            self.head = self.head.getNext()
            removed = "Item Removed"
        else:
            prev = self.head
            curr = prev.getNext()
            while not curr == None:
                if curr.getData() == value:
                    prev.setNext(curr.getNext())
                    removed = "Item Removed"
                prev = curr
                curr = curr.getNext()
        return removed

    def append(self,value):
        curr = self.head
        while not curr.getNext() == None:
            curr = curr.getNext()
        curr.setNext(Node(value))

    def pop(self):
        if self.head == None:
            return "List is Empty"
        else:
            curr = self.head
            while not curr.getNext() == None:
                prev = curr
                curr = curr.getNext()
            prev.setNext(None)
            return "Item Popped"

    def insert(self,pos,value):
        if pos == 0:
            self.add(value)
            return 0
        prev = self.head
        curr = prev.getNext()
        count = 1
        while not count == pos:
            prev = curr
            curr = curr.getNext()
            count += 1
        tempNode = Node(value)
        tempNode.setNext(curr)
        prev.setNext(tempNode)

    def index(self,value):
        curr = self.head
        count = 0
        while curr.getData() != value:
            curr = curr.getNext()
            count+=1
        return count

    def __str__(self):
        string = ""
        curr = self.head
        while not curr == None:
            string += str(curr.getData()) + "->"
            curr = curr.getNext()
        return string[:-2]

if __name__ == "__main__":

    print("\n --------------- Implementation of an Unordered List --------------- \n")
    myList = UnorderedList()
    print("Unordered List is Empty : ", myList.isEmpty())
    myList.add(31)
    myList.add(77)
    myList.add(17)
    myList.add(93)
    myList.add(26)
    myList.add(54)
    print("Size : ",myList.size())
    print("Search 31 : ",myList.search(31))
    print(myList)
    print("Remove 31 : ",myList.remove(31))
    print(myList)
    myList.append(11)
    print(myList)
    print("Unordered List is Empty : ", myList.isEmpty())
    print(myList.pop())
    print(myList)
    print("Insert 25 at [0] & 999 [2]")
    myList.insert(0,25)
    myList.insert(2,999)
    print("Items Inserted Successfully")
    print(myList)
    print("Index of 54 : ",myList.index(54))
    print("\n --------------- END OF UNORDERED LIST --------------- \n")