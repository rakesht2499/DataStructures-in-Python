from QueueApplicationPrograms.RadixSort import RadxiSort

class SortingClass:
    def BubbleSortComplete(self,arrList):
        for x in range(0,len(arrList)-1):
            for y in range(0,len(arrList)-x-1):
                if arrList[y] >= arrList[y+1]:
                    arrList[y],arrList[y+1] = arrList[y+1],arrList[y]

    def BubbleSortStopWhenSorted(self,arrList):
        unSorted,limit = True,len(arrList)
        while unSorted:
            unSorted = False
            limit -= 1
            for y in range(limit):
                if arrList[y] >= arrList[y+1]:
                    unSorted = True
                    arrList[y],arrList[y+1] = arrList[y+1],arrList[y]

    def SelectionSort(self,arrList):
        for pos in range(len(arrList) - 1):
            min = pos
            for i in range(pos + 1, len(arrList)):
                if (arrList[i] < arrList[min]):
                    min = i
            arrList[min], arrList[pos] = arrList[pos], arrList[min]

    def InsertionSort(self,arrList):
        for x in range(len(arrList) - 1):
            check, y = arrList[x + 1], x
            while (arrList[y] > check) and y >= 0:
                arrList[y + 1] = arrList[y]
                y -= 1
            arrList[y + 1] = check

    def ShellSort(self,arrList):
        interval = len(arrList) // 2
        while interval > 0:
            for start in range(interval):
                self.__sortAccording(arrList, start, interval)
            interval //= 2

    def __sortAccording(self,arrList, start, interval):                      #Private Method (Made accessible only for members inside Class for ShellSort)
        for x in range(start + interval, len(arrList), interval):
            pos, value = x, arrList[x]
            while pos >= interval and arrList[pos - interval] > value:
                arrList[pos] = arrList[pos - interval]
                pos -= interval
            arrList[pos] = value

    def MergeSort(self,arrList):
        if len(arrList) > 1:
            mid = len(arrList) // 2
            leftArr = arrList[:mid]
            rightArr = arrList[mid:]
            self.MergeSort(leftArr)
            self.MergeSort(rightArr)
            self.__merge(arrList, leftArr, rightArr)

    def __merge(self,arrList, leftArr, rightArr):                           #Private Method (Made accessible only for members inside Class for MergeSort)
        i, j, k = 0, 0, 0
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
            k, i = k + 1, i + 1
        while j < len(rightArr):
            arrList[k] = rightArr[j]
            k, j = k + 1, j + 1

    def QuickSort(self,arrList):
        self.__performQuickSort(arrList, 0, len(arrList) - 1)

    def __performQuickSort(self,arrList, start, end):                       #Private Method (Made accessible only for members inside Class for QuickSort)
        if start < end:
            splitPoint = self.__partition(arrList, start, end)
            self.__performQuickSort(arrList, start, splitPoint - 1)
            self.__performQuickSort(arrList, splitPoint + 1, end)

    def __partition(self,arrList, start, end):                              #Private Method (Made accessible only for members inside Class for QuickSort)
        pivot, l, r = arrList[start], start + 1, end
        while True:
            while arrList[l] < pivot and l <= r:
                l += 1
            while arrList[r] > pivot and l <= r:
                r -= 1
            if l <= r:
                arrList[l], arrList[r] = arrList[r], arrList[l]
            else:
                arrList[start], arrList[r] = arrList[r], arrList[start]
                break
        return r

    def BucketSort(self,arrList):
        largest, length = max(arrList), len(arrList)
        size = largest // length
        buckets = [[] for _ in range(length)]
        for i in range(length):
            j = arrList[i] // size
            if j != length:
                buckets[j].append(arrList[i])
            else:
                buckets[length - 1].append(arrList[i])
        for i in range(length):
            self.InsertionSort(buckets[i])
        result = []
        for i in range(length):
            result = result + buckets[i]
        return result


    def RadixSorting(self,arrList):
        return RadxiSort(arrList)

if __name__ == "__main__":
    print("\n\n____________ King Of Sorting Class - Implements All forms of Sorting ____________")
    sortObj = SortingClass()
    ListBubble,ListBubble2,ListSelection,ListInsertion,ListShell,ListMerge,ListQuick,ListBucket,ListRadix = [22,99,45,87,1,9,42,66,23],[22,99,45,87,1,9,42,66,23],[22,99,45,87,1,9,42,66,23],[22,99,45,87,1,9,42,66,23],[22,99,45,87,1,9,42,66,23],[22,99,45,87,1,9,42,66,23],[22,99,45,87,1,9,42,66,23],[22,99,45,87,1,9,42,66,23],[22,99,45,87,1,9,42,66,23]
    print("\nBefore Sorting : \t\t\t",ListBubble)
    sortObj.BubbleSortComplete(ListBubble)
    sortObj.BubbleSortStopWhenSorted(ListBubble2)
    sortObj.SelectionSort(ListSelection)
    sortObj.InsertionSort(ListInsertion)
    sortObj.ShellSort(ListShell)
    sortObj.MergeSort(ListMerge)
    sortObj.QuickSort(ListQuick)
    ListBucket = sortObj.BucketSort(ListBucket)     #Note the return Function Carefully
    ListRadix = sortObj.RadixSorting(ListRadix)     #Note the return Function Carefully
    print("\nBubble Sort Complete : \t\t",ListBubble,"\nBubble Sort StopAfterSort : ",ListBubble2,"\nSelectionSort : \t\t\t",ListSelection,"\nInsertion Sort : \t\t\t",ListInsertion,"\nShell Sort : \t\t\t\t",ListShell,"\nMerge Sort : \t\t\t\t",ListMerge,"\nQuick Sort : \t\t\t\t",ListQuick,"\nBucket Sort : \t\t\t\t",ListBucket,"\nRadix Sort (Reverse) : \t\t\t[",ListRadix,"]")

    print("\nNote: We imported the Radix Sort Function from QueueApplication & made a Call to that function from our Class Method, We have returned a Queue in Radix Sort which is why we don't get the list representation\n\n__________ All forms of Sorting Works Perfectly __________")