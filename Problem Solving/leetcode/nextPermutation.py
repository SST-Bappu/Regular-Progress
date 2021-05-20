def nextPermutation(nums):
    n = len(nums)
    i = n-1
    while i>0 and nums[i]<=nums[i-1]:
        i-=1
    if i==0:
        nums.sort()
        return
    keep = i-1
    while i<n and nums[i]>nums[keep]:
        i+=1
    nums[keep],nums[i-1] = nums[i-1],nums[keep]
    left = keep+1
    right = n-1
    while left<right:
        nums[left],nums[right] = nums[right],nums[left]
        left+=1
        right-=1



if __name__=="__main__":
    nums = [1,5,8,4,7,6,5,3,1]
    nextPermutation(nums)
    print(nums)