def insertionsort(list):
    n = len(list)
    for i in range(0,n):
        cmp = list[i]
        keep = -1
        for j in range (i+1,n):
            if list[j]<cmp:
                cmp = list[j]
                keep = j
        if keep>=0:
            tmp = list[i]
            list[i] = list[keep]
            list[keep] = tmp

    print("List after sorting :-\n",list)

#n = int(input("Enter the number how many data you want to insert : "))
list = [14,33,27,10,35,19,42,44]
#for i in range (0,n):
    #x = int (input())
    #list.append(x)

insertionsort(list)