def SearchRatatedArray(nums,target):
    if nums[0] == target:
        return True
    i = 1
    while i<len(nums) and nums[i]>nums[0]:
        if nums[i] == target:
            return True
        i+=1
    return BinarySearch(nums,i,len(nums)-1,target)
def BinarySearch(nums,start,end,target):
    if start>end:
        return False
    mid = (start+end)//2
    if nums[mid] == target:
        return True
    if target>nums[mid]:
        return BinarySearch(nums,mid+1,end,target)
    else:
        return BinarySearch(nums,start,mid-1,target)

if __name__=="__main__":
    nums = [2,5,6,0,0,1,2]
    print(SearchRatatedArray(nums,3))
