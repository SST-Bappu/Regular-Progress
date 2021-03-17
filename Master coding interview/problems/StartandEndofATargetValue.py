class StartandEnd:
    left = right = None
    def __init__(self,list,target):
        self.target = target
        self.list = list
        self.FindStartEnd(0,len(list)-1)
    def FindStartEnd(self,start,end):
        if start>end:
            return
        mid = (start+end)//2
        if self.list[mid]==self.target:
            if self.left==None and self.right==None:
                self.left = self.right = mid
            elif mid>self.right:
                self.right = mid
            elif mid<self.left:
                self.left = mid
            self.FindStartEnd(start,mid-1)
            self.FindStartEnd(mid+1,end)
        elif self.list[mid]<self.target:
            self.FindStartEnd(mid+1,end)
        else:
            self.FindStartEnd(start,mid-1)
def StartandEnd(list,start,end,target):
    mid = (start+end)//2
    if start>end:
        return None, None
    if list[mid]== target:
        left = right = mid
        while(list[left]==target and left>=start):
            left-=1
        while(list[right]==target and right<=end):
            right+=1
        return left+1,right-1
    elif list[mid]>target:
        return StartandEnd(list,start,mid-1,target)
    else:
        return StartandEnd(list,mid+1,end,target)
def BinarySearch(list,start,end,target):
    while(start<=end):
        mid = (start + end) // 2
        if list[mid] == target:
            return mid
        elif list[mid]>target:
            end = mid-1
        else:
            start = mid +1
    return -1
def FindStartEnd(list,target):
    FirstPos = BinarySearch(list,0,len(list)-1,target)
    if FirstPos==-1:
        return [-1,-1]
    left = right = FirstPos
    while(left!=-1):
        temp = left
        left = BinarySearch(list,0,left-1,target)
    left = temp
    while(right!=-1):
        temp = right
        right = BinarySearch(list,right+1,len(list)-1,target)
    right = temp
    return [left,right]

if __name__=="__main__":
    list = [1,1,3,5,6,6,6,7,8]
    #result = StartandEnd(list,4)
    #print(f"Start is = {result.left} and End is = {result.right}")
    result = FindStartEnd(list,7)
    print(f"Start is ={result[0]} and end is ={result[1]}")

