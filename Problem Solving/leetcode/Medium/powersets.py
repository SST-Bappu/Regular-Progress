def powersets(nums):
    result = []
    findSets([],nums,result)
    return result
def findSets(path,nums,result):
    result.append(path)
    if not nums:
        return
    for i in range(len(nums)):
        findSets(path+[nums[i]],nums[i+1:],result)

if __name__=="__main__":
    print(powersets([1]))