def removeElement(nums,val):
    x = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[x] = nums[i]
            x+=1
    return x
if __name__=="__main__":
    nums = [0,1,2,2,3,0,4,2]
    n = removeElement(nums,2)
    for i in range(n):
        print(nums[i])