def MergeSort (list):
    if len(list)<=1:
        return
    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]
    MergeSort(left)
    MergeSort(right)

    merge_two_sorted_array(left,right,list)

def merge_two_sorted_array(a,b,list):
    len_a = len(a)
    len_b = len(b)
    i=j=k=0
    while i<len_a and j<len_b:
        if a[i]<=b[j]:
            list[k] = a[i]
            i+=1
        else:
            list[k] = b[j]
            j+=1
        k+=1
    while i <len_a:
            list[k] = a[i]
            i+=1
            k+=1
    while j<len_b:
            list[k] = b[j]
            j+=1
            k+=1


if __name__ == "__main__":
    list = [10, 3, 15, 7, 8, 23, 98, 29]
    MergeSort(list)
    print(list)