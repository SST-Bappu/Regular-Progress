def insertion_sort(arr):
    i=1
    while i<len(arr):
        if arr[i]<arr[i-1]:
            j=i-1
            while j>=0 and arr[j]>arr[i]:
                j-=1
            arr[j+1],arr[i] = arr[i],arr[j+1]
        else:
            i+=1

#n = int(input("Enter the number how many data you want to insert : "))
list = [14,33,27,10,35,19,42,44]

insertion_sort(list)
print(list)