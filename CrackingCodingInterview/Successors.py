class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def InOrderTraverse(root,traversal):
    if not root:
        return
    InOrderTraverse(root.left,traversal)
    traversal.append(root.data)
    InOrderTraverse(root.right,traversal)
def Successor(root,target):
    Ancestor = None
    chk = 1
    while root:
        RightNode = root.right
        if root.data==target:
            if not root.right:
                return Ancestor
            else:
                RightNode = root.right
                while RightNode.left:
                    RightNode = RightNode.left
                return RightNode
        if target>root.data:
            root = root.right
        else:
            Ancestor = root
            root = root.left
    return None
def FindSuccessor(root,target): #A bit easier code representation but not optimal
    cur = root
    prev = None
    while cur:
        if cur.data>target:
            prev = cur
            cur = cur.left
        else:
            cur = cur.right
    return prev
def insert_bst(root,data):
    if data>root.data:
        if not root.right:
            root.right = Node(data)
            return
        insert_bst(root.right,data)
    else:
        if not root.left:
            root.left = Node(data)
            return
        insert_bst(root.left,data)
if __name__=="__main__":
    list = [10,15,7,9,8,5,12,9,20]
    root = Node(list[0])
    for i in range(1,len(list)):
        insert_bst(root,list[i])
    traversal = []
    InOrderTraverse(root,traversal)
    print(traversal)
    current = Successor(root,8)
    if not current:
        print(current)
    else:
        print(current.data)