class Node:
    def __init__(self,data=None):
        self.data = data
        self.right = None
        self.left = None
def MaxDepth(Head):
    if Head == None:
        return 0
    return 1+max(Head.left,Head.right)

def InsertMinHeap(Head,data):
    if Head == None:
        Head = Node(data)
        return
    h = MaxDepth(Head)
    for i in range(1,h+1):
        Insertion(Head,data,i)
def Insertion(Head,data,Level):
    if Level==1:
        if Head == None:
            Head = Node(data)
        return
    else:
        Insertion(Head.left,data,Level-1)
        Insertion(Head.right,data,Level-1)
