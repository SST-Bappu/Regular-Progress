class QueueByStacks:
    stack1 = []
    stack2 = []
    def Enqueue(self,data):
        self.stack1.append(data)
    def Dequeue(self):
        if len(self.stack2)<=0 and len(self.stack1)>0:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
        elif len(self.stack2)>0:
            return self.stack2.pop()
        else:
            print("List is empty")
    def Display(self):
        if self.stack2:
            print(self.stack2,end=" ")
        print(self.stack1)
if __name__=="__main__":
    Q = QueueByStacks()
    for i in range(5):
        Q.Enqueue(i)
    print(Q.Dequeue())
    print(Q.Dequeue())
    Q.Enqueue(5)
    print(Q.Dequeue())
    print(Q.Dequeue())
    print(Q.Dequeue())
    print(Q.Dequeue())
    Q.Display()