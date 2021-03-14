class ListNode:
    def __init__(self,data=None):
        self.data = data
        self.next = None
        self.prev = None
        self.child = None
def MergeList(node):
    prev = None
    while(node.next!=None):
        if node.child is not None:
            next = node.next
            node.next = node.child
            child = node.child
            child.prev = node
            flat = MergeList(child)
            flat.next = next
            next.prev = flat
            node = next
            prev = flat
        else:
            prev = node
            node = node.next
    return prev

def FlattenDoublyList(node):
    while(node.next!=None):
        if node.child is not None:
            next = node.next
            node.next = node.child
            child = node.child
            child.prev = node
            flat = MergeList(child)
            flat.next = next
            next.prev = flat
            node = next
        else:
            node = node.next

if __name__== "__main__":
    list=[1,2,3,4,5,6]
    listchild1 = [7,8,9]
    listchild2 = [10,11]
    listchild3 = [12,13]
    node = ListNode()
    curNode = node
    prev = None
    for i in list:
        curNode.data = i
        curNode.prev = prev
        prev = curNode
        curNode.next = ListNode()
        if i==2:
            curNode.child = ListNode()
            curChild = curNode.child
            prevChild = None
            for j in listchild1:
                curChild.data = j
                curChild.prev = prevChild
                prevChild = curChild
                curChild.next = ListNode()
                if j==8:
                    curChild.child=ListNode()
                    curCchild = curChild.child
                    prevCchild = None
                    for k in listchild2:
                        curCchild.data = k
                        curCchild.prev = prevCchild
                        prevCchild = curCchild
                        curCchild.next = ListNode()
                        curCchild = curCchild.next
                curChild = curChild.next
        if i==5:
            curNode.child = ListNode()
            curChild = curNode.child
            prevChild = None
            for j in listchild3:
                curChild.data = j
                curChild.prev = prevChild
                prevChild = curChild
                curChild.next=ListNode()
                curChild = curChild.next
        curNode = curNode.next

    curNode = prev
    while(True):
        print(curNode.data, end="->")
        if curNode.child is not None:
            child = curNode.child
            while(True):
                if child.next==None:
                    break
                print(f"-* {child.data}",end=" ")

                if child.child is not None:
                    Cchild = child.child
                    while(True):
                        if Cchild.next==None:
                            break
                        print(f"-*-* {Cchild.data}", end=" ")
                        Cchild = Cchild.next
                child = child.next
            print("->",end=" ")
        if curNode.prev == None:
            break
        curNode = curNode.prev
    print("")
    FlattenDoublyList(node)
    curNode = node
    prev = None
    while(curNode.next!=None):
        print(curNode.data,end="->")
        prev = curNode
        curNode = curNode.next
    curNode = prev
    print("")
    while(True):
        print(curNode.data,end="->")
        if curNode.prev == None:
            break
        curNode = curNode.prev
