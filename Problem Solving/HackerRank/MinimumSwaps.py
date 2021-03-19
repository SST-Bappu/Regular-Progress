count = 0
def MergeSort(arr):
    if len(arr)<=1:
        return
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    MergeSort(left)
    MergeSort(right)

    sorted_array(left,right,arr)

def sorted_array(arr_a,arr_b,arr):
    global count
    a = len(arr_a)
    b = len(arr_b)
    i=j=k=0
    while i<a and j<b:
        if arr_a[i]<=arr_b[j]:
            arr[k] = arr_a[i]
            i+=1
        else:
            arr[k]=arr_b[j]
            j+=1
            count+=1
        k+=1
    while i<a:
        arr[k] = arr_a[i]
        i+=1
        k+=1
    while j<b:
        arr[k] = arr_b[j]
        j+=1
        k+=1
def partition(start,end,list):
    global count
    pivot = start
    while start<=end:
        while start<len(list) and list[start]<=list[pivot]:
            start+=1
        while list[end]>list[pivot]:
            end-=1
        if start<end:
            tmp = list[start]
            list[start] = list[end]
            list[end] = tmp
            count+=1
    tmp = list[pivot]
    list[pivot] = list[end]
    list[end] = tmp
    if pivot != end:
        count+=1
    return end
def Quick_sort(list,start=0,end=-2):
    global count
    if end == -2:
        end = len(list)-1
    if start<end:
        p = partition(start,end,list)
        Quick_sort(list,start,p-1)
        Quick_sort(list,p+1,end)
    return count
def Selection_sort(list):
    cnt = 0
    for i in range(len(list)):
        keep = None
        for j in range(i+1,len(list)):
            if list[j]<list[i]:
                if keep is None:
                    keep = j
                elif list[keep]>list[j]:
                    keep = j
        if keep is not None:
            tmp = list[i]
            list[i] = list[keep]
            list[keep] = tmp
            cnt+=1
    return cnt
def MinimumSwaps(list):
    count = 0
    n = len(list)
    i=0
    while i<n:
        if list[i]!=i+1:
            tmp = list[i]
            chk = tmp-1
            list[i] = list[chk]
            list[chk]=tmp
            count+=1

        else:
            i+=1
    return count



if __name__=="__main__":
    list = [2,31,1,38,29,5,44,6,12,18,39,9,48,49,13,11,7,27, 14, 33, 50, 21, 46, 23, 15, 26, 8, 47, 40, 3, 32, 22, 34, 42, 16, 41, 24, 10, 4, 28, 36, 30, 37, 35, 20, 17, 45, 43, 25, 19]
    #list = [4,3,1,2]
    #MergeSort(list)
    #result=Quick_sort(list)
    result = MinimumSwaps(list)
    print(list)
    print(result)


