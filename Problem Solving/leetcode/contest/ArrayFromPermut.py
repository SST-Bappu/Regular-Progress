def ArrayFromPermut(nums):
    ans = []
    for item in nums:
        ans.append(nums[item])
    return ans
if __name__=="__main__":
    nums = [5,0,1,2,3,4]
    print(ArrayFromPermut(nums))