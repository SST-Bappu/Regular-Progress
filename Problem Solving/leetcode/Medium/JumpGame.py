def JumpGame(nums):
    goal = len(nums)-1
    for i in reversed(range(0,len(nums)-1)):
        if i+nums[i] >= goal:
            goal = i
    return goal==0
if __name__=="__main__":
    nums = [2,3,1,1,4]
    print(JumpGame(nums))