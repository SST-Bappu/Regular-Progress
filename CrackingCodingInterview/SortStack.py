class SortedStack:
    stack =[]
    def Push(self,data):
        if len(self.stack)<=0:
            self.stack.append(data)
        else:
            self.sort(data)
    def pop(self):
        return self.stack.pop()
    def peek(self):
        return self.stack[len(self.stack)-1]
    def isEmpty(self):
        return not(len(self.stack)>0)
    def sort(self,data):
        n = len(self.stack)-1
        if data<self.stack[n]:
            self.stack.append(data)
            return
        self.stack.append(None)
        while(n>=0):
            if data<self.stack[n]:
                self.stack[n+1] = data
                return
            else:
                self.stack[n+1] = self.stack[n]
            n-=1
        self.stack[0]=data
    def Display(self):
        print(self.stack)

def MergeSort(list):
    if len(list)<=1:
        return
    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]
    MergeSort(left)
    MergeSort(right)
    i=j=k=0
    while(j<len(left) and k<len(right)):
        if left[j]>=right[k]:
            list[i]=left[j]
            j+=1
        else:
            list[i]=right[k]
            k+=1
        i += 1
    while(j<len(left)):
        list[i]= left[j]
        j+=1
        i+=1
    while(k<len(right)):
        list[i] = right[k]
        k+=1
        i+=1

if __name__=="__main__":
    list=[3,5,4]
    stack = SortedStack()
    for i in list:
        stack.Push(i)
    stack.Display()
    stack.Push(2)
    stack.Display()
    stack.Push(6)
    stack.Display()