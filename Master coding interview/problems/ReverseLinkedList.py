class listNode:
    def __init__(self,data=0):
        self.data = data
        self.next = None
def listReverse(node):
    prevNode=None
    while(True):
        nextNode = node.next
        node.next = prevNode
        prevNode = node
        node = nextNode
        if node.next == None:
            return prevNode


if __name__=="__main__":
    list=[2,4,8,5,6,10,12]
    node = listNode()
    curNode=node
    for i in list:
        curNode.data = i
        curNode.next = listNode()
        curNode = curNode.next
    curNode = node
    while(True):
        if curNode.next==None:
            break
        print(curNode.data,end="->")
        curNode=curNode.next
    print("")
    curNode=listReverse(node)
    while (True):

        print(curNode.data, end="->")
        if curNode.next == None:
            break
        curNode = curNode.next
