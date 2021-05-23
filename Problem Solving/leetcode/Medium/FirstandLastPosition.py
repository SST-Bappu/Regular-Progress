def firstLast(nums,target):
    first = binarySearch(nums,0,len(nums)-1,target)
    if first == -1:
        return [-1,-1]
    left = right = key = first
    while key!=-1:
        left = key
        key = binarySearch(nums,0,left-1,target)
    key = right
    while key!=-1:
        right = key
        key = binarySearch(nums,right+1,len(nums)-1,target)
    return [left,right]

def binarySearch(nums,start,end,target):
    if start>end:
        return -1
    mid = (start+end)//2
    if nums[mid]==target:
        return mid
    if target>nums[mid]:
        return binarySearch(nums,mid+1,end,target)
    else:
        return binarySearch(nums,start,mid-1,target)

if __name__=="__main__":
    nums = []
    print(firstLast(nums,6))