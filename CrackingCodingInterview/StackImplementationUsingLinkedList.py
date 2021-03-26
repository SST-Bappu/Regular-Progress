class node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
class LinkedList:
    head = None
    Min = []
    def StackPush(self,data):
        if not self.head:
            self.head = node(data)
            self.Min.append(data)
            return
        current = self.head
        while(current.next):
            current = current.next
        current.next = node(data)
        if data<self.Min[len(self.Min)-1]:
            self.Min.append(data)
    def StackPop(self):
        current = self.head
        while(current.next.next):
            current = current.next
        item = current.next.data
        current.next = current.next.next
        if item == self.Min[len(self.Min)-1]:
            self.Min.pop()
        return item
    def Minimum(self):
        return self.Min[len(self.Min)-1]
    def StackPrint(self):
        current = self.head
        while(current):
            print(current.data,end="->")
            current = current.next
        print("")

if __name__=="__main__":
    List = LinkedList()
    arr = [3,4,5,7,8,2,1,0]
    for item in arr:
        List.StackPush(item)
    List.StackPrint()
    print(List.Minimum())
    List.StackPrint()
    print(List.Minimum())

