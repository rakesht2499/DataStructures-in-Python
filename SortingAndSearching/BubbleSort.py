#The complete bubble sort which thge outer loop run's for n times even if the List is sorted before all the iterations

def FullBubbleSort(arrList):
    for x in range(0,len(arrList)-1):
        for y in range(0,len(arrList)-x-1):
            if arrList[y] >= arrList[y+1]:
                arrList[y],arrList[y+1] = arrList[y+1],arrList[y]

#In this case, the looping stops as soon as the List is sorted in any iteraction. Eventhogh it is similar, But time is comparitively less

def BubbleSortStopWhenSorted(arrList):
    unSorted,limit = True,len(arrList)
    while unSorted:
        unSorted = False
        limit -= 1
        for y in range(limit):
            if arrList[y] >= arrList[y+1]:
                unSorted = True
                arrList[y],arrList[y+1] = arrList[y+1],arrList[y]

if __name__ == "__main__":
    arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    arr2 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    FullBubbleSort(arr)
    print("Full Bubble Sort : ",arr)
    BubbleSortStopWhenSorted(arr2)
    print("Stops When Sorted Bubble Sort : ",arr2)