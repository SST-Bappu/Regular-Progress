import copy
import timeit
from itertools import combinations
def threeSum(nums):
    arrangements = []
    nums.sort()
    FindMatch(nums,arrangements)
    return arrangements
def FindMatch(nums,arrangements,cur=[],cnt=0):
    if len(cur)==3 and sum(cur)==0:
        #cur.sort()
        if cur not in arrangements:
            arrangements.append(cur)
        return
    if len(cur)>=3 or cnt>=len(nums):
        return
    for i in range(cnt,len(nums)):
        cur.append(nums[i])
        new = copy.deepcopy(cur)
        FindMatch(nums,arrangements,new,i+1)
        cur.pop()
def threeSum_iter(nums):
    combns = combinations(nums,3)
    arrangements = set()
    for tup in combns:
        tup = sorted(tup)
        if sum(tup)==0:
            arrangements.add(tuple(tup))
    return arrangements
def threeSum_twoPointer(nums):
    nums.sort()
    arrangements = []
    for i in range(len(nums)):
        left = i+1
        right = len(nums)-1
        while left<right:
            sum = nums[i]+nums[left]+nums[right]
            if sum==0:
                if [nums[i],nums[left],nums[right]] not in arrangements:
                    arrangements.append([nums[i],nums[left],nums[right]])
                left+=1
                right-=1
            elif sum<0:
                left+=1
            else:
                right-=1
    return arrangements
def threeSum_optimized(nums):
    nums.sort()
    arrangements = []
    starting=dict()
    for i in range(len(nums)):
        if starting.get(nums[i]):
            continue
        starting[nums[i]] = i
        hash = dict()
        target = -nums[i]
        for j in range(i+1,len(nums)):
            if hash.get(nums[j]) is not None:
                cur= [nums[i],hash[nums[j]],nums[j]]
                if cur not in arrangements:
                    arrangements.append(cur)
            else:
                hash[target-nums[j]] = nums[j]
    return arrangements

if __name__=="__main__":
    nums = [3,-9,3,9,-6,-1,-2,8,6,-7,-14,-15,-7,5,2,-7,-4,2,-12,-7,-1,-2,1,-15,-13,-4,0,-9,-11,7,4,7,13,14,-7,-8,-1,-2,7,-10,-2,1,-10,6,-9,-1,14,2,-13,9,10,-7,-8,-4,-14,-5,-1,1,1,4,-15,13,-12,13,12,-11,12,-12,2,-3,-7,-14,13,-9,7,-11,5,-1,-2,-1,-7,-7,0,-7,-4,1,3,3,9,11,14,10,1,-13,8,-9,13,-2,-6,1,10,-5,-6,0,1,8,4,13,14,9,-2,-15,-13]
    #nums=[-1,0,1,2,-1,-4]
    start = timeit.default_timer()
    result = threeSum(nums)
    print(len(result))
    print(timeit.default_timer()-start)
    start = timeit.default_timer()
    result=threeSum_iter(nums)
    print(len(result))
    print(timeit.default_timer() - start)
    start = timeit.default_timer()
    result=threeSum_twoPointer(nums)
    print(len(result))
    print(timeit.default_timer() - start)

    start = timeit.default_timer()
    result=threeSum_optimized(nums)
    print(len(result))
    print(timeit.default_timer() - start)