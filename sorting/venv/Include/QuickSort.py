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
    i = start
    j=end
    while(i<=j):
        while(list[j]>pivot):
            j-=1
        while(i<=j and list[i]<=pivot):
            i+=1
        if i<j:
            list[i],list[j] = list[j],list[i]

    if start!=j:
        list[j],list[start]=list[start],list[j]
    return j

def QuickSort(list,start,end):
    if start<end:
        p = partition_pivoting_FirstElement(list,start,end)
        QuickSort(list,start,p-1)
        QuickSort(list,p+1,end)


if __name__ == "__main__":
    list = [14, 33, 27, 10, 35, 19, 42, 44]
    #list = [7,1,3,2,4,5,6]
    #list = [2,3,4,1,5]
    QuickSort(list,0,len(list)-1)
    print(list)
