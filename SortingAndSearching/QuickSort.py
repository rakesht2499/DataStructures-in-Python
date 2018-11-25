def quickSort(arrList):
    performQuickSort(arrList,0,len(arrList)-1)

def performQuickSort(arrList,start,end):
    if start<end:
        splitPoint = partition(arrList,start,end)
        performQuickSort(arrList,start,splitPoint-1)
        performQuickSort(arrList,splitPoint+1,end)

def partition(arrList,start,end):
    pivot,l,r = arrList[start],start+1,end
    while True:
        while arrList[l] < pivot and l<=r:
            l+=1
        while arrList[r] > pivot and l<=r:
            r-=1
        if l<=r:
            arrList[l],arrList[r] = arrList[r],arrList[l]
        else:
            arrList[start],arrList[r] = arrList[r],arrList[start]
            break
    return r

if __name__ == "__main__":
    arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    quickSort(arr)
    print(arr)