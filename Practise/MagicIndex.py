def MagicIndex(numbers):
    return FindIndex(numbers,0,len(numbers)-1)
def FindIndex(numbers,start,end):
    if end<start:
        return -1
    mid = (start+end)//2
    if mid == numbers[mid]:
        return mid
    if numbers[mid]>mid:
        return FindIndex(numbers,start,mid-1)
    else:
        return FindIndex(numbers,mid+1,end)
def MagicIndex_NotDistinct(numbers):
    return FindIndex_NotDistinct(numbers,0,len(numbers)-1)

def FindIndex_NotDistinct(numbers,start,end):
    if end<start:
        return None
    mid = (start+end)//2
    if numbers[mid] == mid:
        return mid
    leftIndex = min(mid-1,numbers[mid])
    left = FindIndex_NotDistinct(numbers,start,leftIndex)
    if left:
        return left
    rightIndex = max(mid+1,numbers[mid])
    right = FindIndex_NotDistinct(numbers,rightIndex,end)
    return right

if __name__=="__main__":
    numbers = [-40,-20,-1,1,2,3,5,7,9,12,13]
    list = [1,2,2,2,2,4,7,8]
    print(MagicIndex(numbers))
    print(MagicIndex_NotDistinct(list))