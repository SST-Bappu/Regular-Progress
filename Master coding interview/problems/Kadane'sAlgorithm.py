def maxSubArray(list):
    return kadane(list,len(list)-1)

def kadane(list,n,maxS=0):
    if n==0:
        maxS = list[0]
        return list[0]
    sub = kadane(list,n-1)
    maxS = max()
    return max(list[n],list[n]+sub)

if __name__=="__main__":
    list = [1,-3,2,1,-1]
    print(maxSubArray(list))