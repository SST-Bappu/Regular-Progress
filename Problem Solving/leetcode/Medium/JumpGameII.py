def JumpGame2(nums):
   if len(nums) == 1:
        return 0
   left = right = 0
   steps = 1
   while (right + nums[right])<len(nums)-1:
       maxJ = left+1
       steps+=1
       for i in range(left+1,right+nums[right]+1):
           if i+nums[i]>nums[maxJ]+maxJ:
               maxJ = i
       left =right + nums[right]
       right = maxJ
   return steps
if __name__=="__main__":
    nums = [2,3,0,1,4]
    print(JumpGame2(nums))
