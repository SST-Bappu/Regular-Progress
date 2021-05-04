import sys
def ThreeSumClosest(nums,target):
    nums.sort()
    arrangements = []
    starting = dict()
    closest = -sys.maxsize
    for i in range(len(nums)):
        if starting.get(nums[i]):
            continue
        starting[nums[i]] = i
        hash = dict()
        target = -nums[i]
        for j in range(i + 1, len(nums)):
            if hash.get(nums[j]) is not None:
                cur = [nums[i], hash[nums[j]], nums[j]]
                if cur not in arrangements:
                    arrangements.append(cur)
            else:
                hash[target - nums[j]] = nums[j]
    return arrangements
