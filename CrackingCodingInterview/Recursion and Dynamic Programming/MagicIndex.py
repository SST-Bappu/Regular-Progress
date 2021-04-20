def MagicIndex(list):
    return LevBinarySearch(list,0,len(list))

def LevBinarySearch(list,start,end): #It works if all the items are distinct
    if end<start:
        return
    mid = (start+end)//2
    if mid == list[mid]:
        return mid
    if list[mid]<mid:
        return LevBinarySearch(list,mid+1,end)
    else:
        return LevBinarySearch(list,start,mid-1)
#if list items are not distinct, above algorithm is not going to work. Code below is for the non-distinct list item
def FindIndex(list,start,end):
    if end<start:
        return
    mid = (start+end)//2
    if mid == list[mid]:
        return mid
    result = []
    leftIndex = min(mid-1,list[mid])
    left = FindIndex(list,start,leftIndex)
    if left:
        result.append(left)
    rightIndex = max(mid+1,list[mid])
    right = FindIndex(list,rightIndex,end)
    if right:
        result.append(right)
    return result
if __name__=="__main__":
    list=[-40,-20,-1,1,2,3,5,7,9,12,13]
    print(MagicIndex(list))
    list1 = [-10,-5,2,2,2,3,4,7,9,12,13]
    print(FindIndex(list1,0,len(list1)))