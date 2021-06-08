def MaxSubArray(nums):
    maxSum = cur = nums[0]
    right = 1
    while right < len(nums):
        while right<len(nums) and nums[right]<=cur:
            cur += nums[right]
            maxSum = max(maxSum,cur)
            right+=1
        if right<len(nums):
            cur = max(cur+nums[right],nums[right])
            maxSum = max(maxSum, cur)
            right += 1
    return maxSum
if __name__=="__main__":
    nums = [1,2]
    print(MaxSubArray(nums))