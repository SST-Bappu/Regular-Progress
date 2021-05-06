import sys
def ThreeSumClosest(nums,target):
    nums.sort()
    starting = dict()
    closest = sys.maxsize
    result = None
    for i in range(len(nums)):
        if starting.get(nums[i]):
            continue
        starting[nums[i]] = i
        left = i+1
        right = len(nums)-1
        while left<right:
            sum = nums[i]+nums[left]+nums[right]
            if abs(target-sum)<closest:
                closest = abs(target-sum)
                result = sum
            closest= min(closest,abs(target-sum))
            if sum<=target:
                left+=1
            else:
                right-=1
    return result
if __name__=="__main__":
    nums = [-1,2,1,-4]
    print(ThreeSumClosest(nums,1))