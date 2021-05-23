def InsertPosition(nums,target):
    return binarySearch(nums,0,len(nums)-1,target)
def binarySearch(nums,start,end,target):
    if start>end:
        return -1
    mid = (start+end)//2
    if nums[mid] == target:
        return mid
    if target>nums[mid]:
        k = binarySearch(nums,mid+1,end,target)
        if k == -1:
            return mid+1
    else:
        k = binarySearch(nums,start,mid-1,target)
        if k == -1:
            return start
    return k

if __name__=="__main__":
    nums = [1]
    print(InsertPosition(nums,0))
