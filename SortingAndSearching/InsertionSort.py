def InsertionSort(arrList):
    for x in range(len(arrList)-1):
        check,y = arrList[x+1],x
        while (arrList[y] > check) and y >= 0:
            arrList[y+1] = arrList[y]
            y -= 1
        arrList[y+1] = check

if __name__ == "__main__":
    arr = [54,26,93,17,77,31,44,55,20]
    InsertionSort(arr)
    print(arr)