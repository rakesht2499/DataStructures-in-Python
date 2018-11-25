def SelectionSort(arrList):
    for pos in range(len(arrList)-1):
        min = pos
        for i in range(pos+1,len(arrList)):
            if(arrList[i] < arrList[min]):
                min = i
        arrList[min],arrList[pos] = arrList[pos],arrList[min] #Swapping with the Min Element

if __name__ == "__main__":
    arr = [54,26,93,17,77,31,44,55,20]
    SelectionSort(arr)
    print(arr)