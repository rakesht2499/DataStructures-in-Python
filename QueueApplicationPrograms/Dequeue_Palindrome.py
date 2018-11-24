from DataStructures.LinearDS import Dequeue

def checkPalindrome(arr):
    charDq = Dequeue()
    for x in arr:
        charDq.addFront(x)
    while charDq.size() > 1:
        front = charDq.removeFront()
        rear = charDq.removeRear()
        if front != rear:
            return False
    return True

print(checkPalindrome("lsdkjfskf"))
print(checkPalindrome("radar"))