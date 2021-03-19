def BinarySearch(arr,t,left=0,right=None):
    if right==None:
        right=len(arr)-1
    if left>right:
        return None
    mid = (left+right)//2
    if arr[mid]==t:
        return mid
    if t>arr[mid]:
        return BinarySearch(arr,t,mid+1,right)
    else:
        return BinarySearch(arr,t,left,mid-1)

if __name__=="__main__":
    list=[1,2,3,4,5,6,7,8]
    res = BinarySearch(list,3)
    if res==None:
        print("Item not Found..!")
    else:
        print(f"Item found at index {res}")