def SumMinProduct(nums):
    left = 0
    right = len(nums)-1
    maxS = nums[0]*nums[0]
    while left <= right:
        newList = nums[left:right+1]
        cur = min(newList)*sum(newList)
        maxS = max(maxS,cur)
        if nums[left]>nums[right]:
            right -= 1
        elif nums[left] == nums[right]:
            if (left+1<right-1) and nums[left+1]>nums[right-1]:
                right -= 1
            else:
                left+=1
        else:
            left += 1
    return maxS
if __name__=="__main__":
    #nums = [4,1,1,1,2,2,5,1,5,5]
    nums = [2,5,4,2,4,5,3,1,2,4]
    print(SumMinProduct(nums))