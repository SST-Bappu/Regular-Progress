from collections import deque
class BinaryTree:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None
def InsertNode(head,data):
    if head.data==None:
        head.data = data
        return
    if data==head.data:
        print("Duplicate Entry isn't allowed")
        return
    if data > head.data:
        if not head.right:
            head.right = BinaryTree()
        InsertNode(head.right,data)
    else:
        if not head.left:
            head.left=BinaryTree()
        InsertNode(head.left,data)
def MaximumDepth(Head):
    if Head == None:
        return 0
    return 1+max(MaximumDepth(Head.left),MaximumDepth(Head.right))
def PreOrderTraversal(Head):
    if Head == None:
        return
    print(Head.data,end="->")
    PreOrderTraversal(Head.left)
    PreOrderTraversal(Head.right)
def PostOrderTraversal(Head):
    if Head==None:
        return
    PostOrderTraversal(Head.left)
    PostOrderTraversal(Head.right)
    print(Head.data, end ="->")
def InOrderTraversal(Head):
    if Head == None:
        return
    InOrderTraversal(Head.left)
    print(Head.data,end="->")
    InOrderTraversal(Head.right)
def BFS(Head):
    if Head == None:
        return
    h = MaximumDepth(Head)
    for i in range(1,h+1):
        TraverseLevelOrder(Head,i)
        print()
def TraverseLevelOrder(Head,Level):
    if Head==None:
        return
    if Level==1:
        print(Head.data, end="->")
    else:
        TraverseLevelOrder(Head.left,Level-1)
        TraverseLevelOrder(Head.right,Level-1)
def BFS_with_deque(root):
    if not root:
        return
    Q = deque()
    Q.append(root)
    while len(Q):
        count = 0
        n = len(Q)
        while count<n:
            current = Q.popleft()
            print(current.data,end="->")
            if current.left:
                Q.append(current.left)
            if current.right:
                Q.append(current.right)
            count+=1
        print()
def Remove(Head):
    if Head.left==None:
        return Head
    else:
        return Remove(Head.left)
def RemoveEntry(Head,data):
    if data>Head.data:
        Head.right = RemoveEntry(Head.right,data)
    elif data<Head.data:
        Head.left=RemoveEntry(Head.left,data)
    else:
        if Head.right == None:
            temp = Head.left
            Head = None
            return temp
        elif Head.left==None:
            temp = Head.right
            Head = None
            return temp
        else:
            current = Remove(Head.right)
            Head.data = current.data
            Head.right=(RemoveEntry(Head.right,current.data))
    return Head


if __name__=="__main__":
    list = [5,8,7,6,3,4,2,10,2]
    Head = BinaryTree()
    i=0
    while(i<len(list)):
        InsertNode(Head,list[i])
        i+=1
    # print("Maximum Depth is = ",MaximumDepth(Head))
    # InOrderTraversal(Head)
    # print("")
    #RemoveEntry(Head,5)
    #print("Tree after Removing Data")
    BFS(Head)
    print("BFS using deque")
    BFS_with_deque(Head)

