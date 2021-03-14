def ArrayDS(arr):
    i=0
    maxVal = None
    while(len(arr)-i>=3):
        j = 0
        while(len(arr)-j>=3):
            val=arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]+arr[i+1][j+1]
            if maxVal==None:
                maxVal = val
            else:
                maxVal=max(maxVal,val)
            print(f"i = {i} and val = {val} and maxVal={maxVal}")
            j+=1
        i+=1
    return maxVal
if __name__=="__main__":
    #list=[[1,1,1,0,0,0],[0,1,0,0,0,0],[1,1,1,0,0,0],[0,0,2,4,4,0],[0,0,0,2,0,0],[0,0,1,2,4,0]]
    list = [[-1, 1, -1, 0, 0, 0], [0, -1, 0, 0, 0, 0], [-1, -1, -1, 0, 0, 0], [0, -9, 2, -4, -4, 0], [-7, 0, 0, -2, 0, 0],
            [0, 0, -1, -2, -4, 0]]
    print(ArrayDS(list))
