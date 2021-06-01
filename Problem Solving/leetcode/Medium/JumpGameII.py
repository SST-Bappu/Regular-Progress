import sys
def JumpGame2(nums):
    def BottomUp(i,steps):
        if i==len(nums)-1:
            return steps
        if i>=len(nums):
            return sys.maxsize
        if nums[i]==0:
            return sys.maxsize
        result = sys.maxsize
        for j in reversed(range(1,nums[i]+1)):
                result = min(result,BottomUp(i+j,steps+1))
        return result
    return BottomUp(0,0)
if __name__=="__main__":
    nums = [5,6,4,4,6,9,4,4,7,4,4,8,2,6,8,1,5,9,6,5,2,7,9,7,9,6,9,4,1,6,8,8,4,4,2,0,3,8,5]
    print(JumpGame2(nums))
