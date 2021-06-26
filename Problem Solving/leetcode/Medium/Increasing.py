def increasing(nums):
    cnt = 0
    for i in range(1,len(nums)):
        if nums[i]<=nums[i-1]:
            if not cnt:
                if i-2>=0:
                    if nums[i] < nums[i-2]:
                        nums[i] = nums[i-1]+1
                else:
                    nums[i-1] = min(nums[i],nums[i-1])-1
            cnt+=1
            if cnt>1:
                return False
    return True
if __name__== "__main__":
    nums = [10,100,21,100]
    print(increasing(nums))