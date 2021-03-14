def rotLeft(arr,d):
    for i in range(d):
        item = arr[0]
        arr.pop(0)
        arr.append(item)
    return arr
def Solution_Optimized(arr,d):
    arr = arr[d:]+arr[:d]
    return arr
if __name__=="__main__":
    list =[]
    n=5
    for i in range(n):
        list.append(i+1)
    print(list)
    list1 = list
    #print(rotLeft(list,2))
    print(Solution_Optimized(list1,4))