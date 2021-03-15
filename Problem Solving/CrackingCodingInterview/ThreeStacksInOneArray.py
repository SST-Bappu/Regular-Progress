class stack:
    def __init__(self,start,end,list):
        self.start = start
        self.end = end
        self.list = list
        self.top = start
    def push(self,data):
        if self.top<=self.start:
            self.list[self.start] = data
            self.top += 1
        elif self.top>=self.end:
            print("Overflow")
        else:
            self.list[self.top]=data
            self.top+=1
    def pop(self):
        if self.top<=0:
            print("Stack is empty")
        else:
            self.list[self.top-1]=None
            self.top-=1

if __name__=="__main__":
    list = [None]*12
    n= len(list)
    stack1 = stack(0,n//3,list)
    stack2 = stack(n//3,(2*n)//3,list)
    stack3 = stack((2*n)//3,n,list)
    stack2.push(10)
    stack2.push(20)
    stack2.push(30)
    stack2.push(40)
    stack2.pop()
    stack2.pop()
    stack2.push(50)
    stack2.pop()
    print(list)
    stack1.pop()