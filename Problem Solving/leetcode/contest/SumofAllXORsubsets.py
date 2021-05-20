def XORsubsets(nums):
    subsets = [[]]
    FindSubsets(nums,subsets)
    return XORoperation(subsets)

def XORoperation(subsets):
    sum = 0
    for set in subsets:
        if not len(set):
            continue
        if len(set)==1:
            sum+=set[0]
            continue
        for i in range(1,len(set)):
            set[i]= set[i]^set[i-1]
        sum+=set[len(set)-1]
    return sum

def FindSubsets(nums,subsets):
    for num in nums:
        n = len(subsets)
        i=0
        while i<n:
            subsets.append(subsets[i]+[num])
            i+=1
if __name__=="__main__":
    nums = [1,3]
    print(XORsubsets(nums))
