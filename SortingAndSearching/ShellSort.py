def shellSort(arrList):
    interval = len(arrList)//2
    while interval > 0:
        for start in range(interval):
            sortAccording(arrList,start,interval)
        interval //= 2

def sortAccording(arrList,start,interval):
    for x in range(start+interval,len(arrList),interval):
        pos,value = x,arrList[x]
        while pos >= interval and arrList[pos-interval] > value:
            arrList[pos] = arrList[pos-interval]
            pos -= interval
        arrList[pos] = value

if __name__ == "__main__":
    arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    shellSort(arr)
    print(arr)