def StartAndEnd(list,item):
    firstpos = BinarySearch(list,0,len(list)-1,item)
    if firstpos==-1:
        return [-1,-1]
    left = right = firstpos
    while left!=-1:
        temp = left
        left = BinarySearch(list,0,left-1,item)
    left = temp
    while right!=-1:
        temp = right
        right = BinarySearch(list,right+1,len(list)-1,item)
    right = temp
    return [left,right]

def BinarySearch(list,start,end,item):
    if start>end:
        return-1
    mid = (start+end)//2
    if list[mid]==item:
        return mid
    elif list[mid]<item:
        return BinarySearch(list,mid+1,end,item)
    else:
        return BinarySearch(list,start,mid-1,item)

if __name__=="__main__":
    list=[2,3,4,4,4,4,5,8]
    print(StartAndEnd(list,2))

