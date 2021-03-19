def FindDuplicate(arr):
    for i in range(len(arr)):
        if arr[abs(arr[i])]>=0:
            arr[abs(arr[i])]=-arr[abs(arr[i])]
        else:
            print(abs(arr[i]))

if __name__=="__main__":
    arr = [1,2,3,6,3,6,1]
    FindDuplicate(arr)