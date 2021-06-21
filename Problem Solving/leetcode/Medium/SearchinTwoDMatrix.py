def SearchIn2Dmatrix(matrix,target):
    m = len(matrix)
    n = len (matrix[0])
    for i in range(m):
        if target <= matrix[i][-1]:
            return BinarySearch(matrix[i],0,n-1,target)
    return False

def BinarySearch(nums,left,right,target):
    if left>right:
        return False
    mid = (left+right)//2
    if nums[mid] == target:
        return True
    if nums[mid]>target:
        return BinarySearch(nums,left,mid-1,target)
    else:
        return BinarySearch(nums,mid+1,right,target)

if __name__=="__main__":
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    print(SearchIn2Dmatrix(matrix,13))