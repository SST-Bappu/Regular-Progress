def partition_pivoting_LastElement(list,start,end):
    pivot = list[end]
    i = j = start
    while(j<=end):
        if list[j]<=pivot:
            list[i], list[j] = list[j], list[i]
            i+=1
        j+=1
    #list[i],list[end] = list[end],list[i]
    return i-1
def QuickSort(list, start, end, idx):
    if start < end:
        p = partition_pivoting_LastElement(list, start, end)
        if p==idx:
            return list[idx]
        elif p>idx:
            return QuickSort(list,start,p-1,idx)
        else:
            return QuickSort(list,p+1,end,idx)
if __name__=="__main__":
    list = [2,3,1,6,4,5]
    idx = len(list)-4
    print("K'th Largest Element is = ",QuickSort(list,0,len(list)-1,idx))
    print(list)
