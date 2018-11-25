from SortingAndSearching.InsertionSort import InsertionSort
def BucketSort(arrList):
    largest,length = max(arrList),len(arrList)
    size = largest//length
    buckets = [[] for _ in range(length)]
    for i in range(length):
        j = arrList[i]//size
        if j != length:
            buckets[j].append(arrList[i])
        else:
            buckets[length - 1].append(arrList[i])
    for i in range(length):
        InsertionSort(buckets[i])
    result = []
    for i in range(length):
        result = result + buckets[i]
    return result

if __name__ == "__main__":
    print(BucketSort([54, 26, 93, 17, 77, 31, 44, 55, 20]))