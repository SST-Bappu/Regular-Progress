def FirstMissingPositive(nums):
    n = len(nums)
    for i in range(n):
        while (nums[i]-1 in range(n)) and (nums[i]!=nums[nums[i]-1]):
            nums[nums[i]-1],nums[i] = nums[i],nums[nums[i]-1]
            print(nums)
    return next((i+1 for i,num in enumerate(nums) if nums[i]!=i+1),n+1)

if __name__=="__main__":
    nums = [3,4,-1,1]
    print(FirstMissingPositive(nums))