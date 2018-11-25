def mergeSort(arrList):
    if len(arrList) > 1:
        mid = len(arrList)//2
        leftArr = arrList[:mid]
        rightArr = arrList[mid:]
        mergeSort(leftArr)
        mergeSort(rightArr)
        merge(arrList,leftArr,rightArr)

def merge(arrList,leftArr,rightArr):
    i,j,k = 0,0,0
    while i < len(leftArr) and j < len(rightArr):
        if leftArr[i] < rightArr[j]:
            arrList[k] = leftArr[i]
            i += 1
        else:
            arrList[k] = rightArr[j]
            j += 1
        k += 1
    while i < len(leftArr):
        arrList[k] = leftArr[i]
        k,i = k+1,i+1
    while j < len(rightArr):
        arrList[k] = rightArr[j]
        k, j = k + 1, j + 1

if __name__ == "__main__":
    arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    mergeSort(arr)
    print(arr)