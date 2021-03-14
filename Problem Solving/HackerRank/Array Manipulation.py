def arrayManipulation(n,arr):
    list=[]
    maxVal = 0
    for j in range(len(arr)):
        row = []
        for i in range(n):
            if (i+1)>= arr[j][0] and (i+1)<=arr[j][1]:
                if j>0:
                    val = list[j-1][i] + arr[j][2]
                    maxVal = max(maxVal,val)
                    row.append(val)
                else:
                    row.append(arr[j][2])
            else:
                if j>0:
                    row.append(list[j-1][i])
                else:
                    row.append(0)
        list.append(row)
    for row in list:
        for item in row:
            print(item, end =" ")
        print("")
    return maxVal
def Optimized(n,arr):
    res = [0]*(n+2)
    for a,b,k in arr:
        res[a]+=k
        res[b+1]-=k
    max = val =0
    print(res)
    for i in res:
        val+=i
        if val>max:
            max = val
    return max



if __name__=="__main__":
    list=[[1,5,3],[4,8,7],[6,9,1]]
    #list =[[1,2,100],[2,5,100],[3,4,100]]
    result = Optimized(10,list)
    print(result)