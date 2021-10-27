class ListNode:
    def __init__(self,data=None):
        self.data = data
        self.next = None
        self.prev = None
        self.child = None
def DetectCycle(node):
    HashTable = dict()
    prev = node
    while(node.next!=None):
        if HashTable.get(node)==None:
            HashTable.update({node: node.data})
            prev = node
            node=node.next
        else:
            prev.next = None
            return
def FloydCycleDetection(node):
    slow = node
    fast = node
    while(True):
        slow = slow.next
        fast = fast.next.next
        if (slow.next==None or fast.next==None):
            print("There's no Cycle")
            return
        if slow == fast:
            slow = node
            break
    while(slow.next!=fast.next):
        slow = slow.next
        fast = fast.next
    fast.next=None




if __name__== "__main__":
    list=[1,2,3,4,5,6,7,8,9]
    node = ListNode()
    curNode = node
    prev = None
    for i in list:
        curNode.data = i
        curNode.prev = prev
        prev = curNode
        curNode.next = ListNode()
        if i==2:
            keep = curNode
        curNode = curNode.next
    prev.next = keep
    FloydCycleDetection(node)
    curNode = node
    while(curNode):
        print(curNode.data, end="->")
        curNode = curNode.next

