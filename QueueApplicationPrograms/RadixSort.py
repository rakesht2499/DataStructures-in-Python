from DataStructures.LinearDS import Queue

def RadxiSort(arr):
    bin_main,bin = Queue(),[Queue(),Queue(),Queue(),Queue(),Queue(),Queue(),Queue(),Queue(),Queue(),Queue()]
    for x in arr:
        bin_main.enqueue(x)
    for x in range(len(str(max(arr)))):
        for _ in range(len(arr)):
            popped_item = bin_main.dequeue()
            bin[(popped_item//(10**x))%10].enqueue(popped_item)
        for i in bin:
            while not i.isEmpty():
                bin_main.enqueue(i.dequeue())
    return bin_main

print(RadxiSort([5,1,78,234,5774,23]))