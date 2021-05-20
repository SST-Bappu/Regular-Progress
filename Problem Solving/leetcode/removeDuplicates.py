def removeDuplicates(nums):
    n = len(nums)
    for i in range(n):
        j=i+1
        while j<n and nums[j]==nums[i]:
            nums.pop(j)
            n-=1
    return len(nums)
def removeDuplicates_optimized(nums):
    x = 1
    for i in range(len(nums)-1):
        if nums[i]!=nums[i+1]:
            nums[x] = nums[i+1]
            x+=1
    return x

if __name__=="__main__":
    nums = [0,0,1,1,1,2,2,3,3,4]
    print(removeDuplicates_optimized(nums))