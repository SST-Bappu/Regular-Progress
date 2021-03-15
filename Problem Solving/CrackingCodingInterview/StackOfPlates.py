class StackofPlates:
    stack = []
    temp = []
    n=top=0
    def push(self,data):
        if self.top>=10:
            self.stack.append(self.temp)
            self.n+=1
            self.top = 0
            self.temp=[]
        self.temp.append(data)
        self.top+=1
    def pop(self):
        if len(self.temp)>0:
            self.temp.pop()
            self.top-=1
            if self.top==0:
                self.top = 10
        elif self.n-1>=0:
            self.stack[self.n-1].pop()
            self.top-=1
            if self.top==0:
                self.top=10
                self.n-=1
        else:
            print("Stack is empty")

    def DisplayStack(self):
        for row in self.stack:
            print(row)
        print(self.temp)
if __name__=="__main__":
    stack = StackofPlates()
    for i in range(21):
        stack.push(i)
    for i in range(15):
        stack.pop()
    stack.DisplayStack()
