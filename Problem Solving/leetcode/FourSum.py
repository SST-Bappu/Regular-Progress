def FourSum(nums,target):
    nums.sort()
    first = {}
    arrangements = []
    for i in range(len(nums)):
        if first.get(nums[i]):
            continue
        first[nums[i]] = i
        second = {}
        for j in range(i+1,len(nums)):
            if second.get(nums[j]):
                continue
            second[nums[j]] = j
            left = j+1
            right = len(nums)-1
            hash = {}
            key = target - (nums[i]+nums[j])
            for k in range(j+1,len(nums)):
                if hash.get(nums[k])!=None:
                    cur = [nums[i],nums[j],hash[nums[k]],nums[k]]
                    if cur not in arrangements:
                        arrangements.append(cur)
                else:
                    var = key - nums[k]
                    hash[var] = nums[k]
    return arrangements

if __name__=="__main__":
    # nums = [1,0,-1,0,-2,2]
    nums = [2,2,2,2,2]
    print(FourSum(nums,8))

