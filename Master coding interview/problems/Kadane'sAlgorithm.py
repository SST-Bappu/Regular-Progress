import copy
def maxSubarray(list):
    maxS = [list[0]]
    maxC = [list[0]]
    for i in range(1, len(list)):
        if sum(maxC+[list[i]])>list[i]:
            maxC+=[list[i]]
        else:
            maxC = [list[i]]
        if sum(maxC) > sum(maxS):
            maxS = copy.deepcopy(maxC)
    return maxS
def maxSumSubArray(list): #Kadane's algorithm to find Maximum sum of contiguous subarray of an array
    maxS = maxC = list[0]
    for i in range(1,len(list)):
        maxC = max(list[i],list[i]+maxC)
        if maxC>maxS:
            maxS = maxC
    return maxS

if __name__=="__main__":
    list = [3,-1,5,6,-4,2]
    print(maxSubarray(list))
    print(maxSumSubArray(list))