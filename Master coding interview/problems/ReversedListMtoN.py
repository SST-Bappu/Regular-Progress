class listNode:
    def __init__(self,data=0):
        self.data = data
        self.next = None
def listReverse(node,m,n):
    cnt = 1
    curNode = node
    NodeE = curNode
    while(True):
        if cnt ==m:
            break
        else:
            cnt+=1
            NodeE = curNode
            curNode = curNode.next
    prevNode=None
    curANode = curNode
    while(True):
        nextNode = curANode.next
        curANode.next = prevNode
        prevNode = curANode
        if cnt == n:
            NodeE.next = prevNode
            curNode.next=nextNode
            break
        curANode = nextNode
        cnt+=1
    if m==1:
        return prevNode
    else:
        return NodeE


if __name__=="__main__":
    list=[1,2,3,4,5,6]
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
    m=2
*    n=6
    curNode=listReverse(node,m,n)
    while (True):
        if curNode.next == None:
            break
        print(curNode.data, end="->")
        curNode = curNode.next
