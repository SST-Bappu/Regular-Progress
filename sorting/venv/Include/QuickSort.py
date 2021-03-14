def partition(list,start,end):
    pivot = list[start]
    pivot_index = start
    while start<=end:
        while start<len(list) and list[start]<=pivot:
            start+=1
        while list[end]>pivot:
            end-=1
        if start<end:
            tmp = list[start]
            list[start] = list[end]
            list[end] = tmp
    tmp = list[pivot_index]
    list[pivot_index] = list[end]
    list[end] = tmp
    return end

def QuickSort(list,start,end):
    if start<end:
        p = partition(list,start,end)
        QuickSort(list,start,p-1)
        QuickSort(list,p+1,end)


if __name__ == "__main__":
    #list = [14, 33, 27, 10, 35, 19, 42, 44]
    #list = [7,1,3,2,4,5,6]
    list = [2,3,4,1,5]
    QuickSort(list,0,len(list)-1)
    print(list)
