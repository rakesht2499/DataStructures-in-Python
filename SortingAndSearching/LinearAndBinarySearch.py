def linearSearch(arrList,item):
    for x in arrList:
        if x == item:
            return True
    return False

def binarySearch(arrList,item):
    start,end = 0,len(arrList)-1
    while start<=end:
        mid = (start+end)//2
        if arrList[mid] == item:
            return True
        elif item > arrList[mid]:
            start = mid+1
        else:
            end = mid-1
    return False

if __name__ == "__main__":
    print("____________Linear Search____________")
    print(linearSearch([56,23,87,12,6,3,2,9],87))
    print(linearSearch([56,23,87,12,6,3,2,9],98))
    print("____________Binary Serach____________")
    print(binarySearch([11,22,33,44,55,66,77,88],77))
    print(binarySearch([11, 22, 333, 44, 55, 66, 77, 88], 99))