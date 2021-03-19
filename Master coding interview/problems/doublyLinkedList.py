class ListNode:
    def __init__(self,data=None):
        self.data = data
        self.prev = None
        self.next = None

if __name__=="__main__":
    list =[1,2,3,4,5,6]
    node = ListNode()
    curNode = node
    prev = None
    for i in list:
            curNode.data=i
            curNode.prev = prev
            curNode.next=ListNode()
            prev = curNode
            curNode=curNode.next
    curNode = node
    while(True):
        if curNode.data==None:
            break
        print(curNode.data, end="->")
        curNode=curNode.next
    print("")
    curNode=prev
    while(True):
        print(curNode.data, end="->")
        if curNode.prev==None:
            break
        curNode=curNode.prev





