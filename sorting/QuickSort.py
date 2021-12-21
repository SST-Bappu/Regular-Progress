from datetime import  datetime
def partition(list,start,end):
    pivot = list[start]
    pivot_index = start
    while start<=end:
        while start<len(list) and list[start]<=pivot:
            start+=1
        while list[end]>pivot:
            end-=1
        if start<end:
            list[start],list[end] = list[end],list[start]
    list[pivot_index],list[end]=list[end],list[pivot_index]
    return end
def partition_pivoting_LastElement(list,start,end):
    pivot = list[end]
    i = j = start
    while(j<end):
        if list[j]<=pivot:
            list[i], list[j] = list[j], list[i]
            i+=1
        j+=1
    list[i],list[end] = list[end],list[i]
    return i

def partition_pivoting_FirstElement(list,start,end):
    pivot = list[start]
    i = j = end
    while(j>start):
        if list[j]>pivot:
            list[i],list[j] = list[j],list[i]
            i-=1
        j-=1
    list[i],list[start] = list[start],list[i]
    return i

def QuickSort(list,start,end):
    if start<end:
        p = partition_pivoting_FirstElement(list,start,end)
        QuickSort(list,start,p-1)
        QuickSort(list,p+1,end)

def quicksort_different(arr): #an unique way to quick sort
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort_different(left) + middle + quicksort_different(right)


if __name__ == "__main__":
    #list = [14, 33, 27, 10, 35, 19, 42, 44]
    #list = [7,1,3,2,4,5,6]
    list = [2,3,4,1,5]
    now = datetime.now()
    QuickSort(list,0,len(list)-1)
    print(datetime.now()-now)
    print(list)
    now = datetime.now()
    quicksort_different(list)
    print(datetime.now()-now)
    print(list)