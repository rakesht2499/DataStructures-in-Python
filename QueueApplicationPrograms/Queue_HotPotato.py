from DataStructures.LinearDS import Queue

def hotPotato(arr,num):
    potato = Queue()
    for x in arr:
        potato.enqueue(x)
    while not potato.size() == 1:
        for _ in range(num):
            potato.enqueue(potato.dequeue())
        potato.dequeue()
    return potato.dequeue()

if __name__ == "__main__":
    print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))