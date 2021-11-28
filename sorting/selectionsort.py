def SelectionSort(list):
    n = len(list)
    for i in range (1,n):
        for j in range (i,0,-1):
            if list[j - 1] > list[j]:
                tmp = list[j]
                list[j] = list[j-1]
                list[j-1] = tmp
                print(list)
            else:
                break
    print(list)

list = [14,33,27,10,35,19,42,44]
print(list)
SelectionSort(list)
print(list)