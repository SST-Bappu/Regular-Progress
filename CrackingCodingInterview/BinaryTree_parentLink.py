from collections import deque
#Every child will have link to its parent
class BinaryTree:
    def __init__(self,data=None,parent=None):
        self.data = data
        self.right = None
        self.left = None
        self.parent = parent
def insertion(tree, data):
    Q = deque()
    if tree.data==None:
        tree.data = data
        return
    Q.append(tree)
    while len(Q):
        count = 0
        n = len(Q)
        while count<n:
            current = Q.popleft()
            if current.left==None:
                current.left = BinaryTree(data,current)
                return
            else:
                Q.append(current.left)
            if current.right == None:
                current.right = BinaryTree(data,current)
                return
            else:
                Q.append(current.right)
            count+=1
def Display(tree):
    Q = deque()
    Q.append(tree)
    while len(Q):
        count = 0
        n = len(Q)
        while count<n:
            current = Q.popleft()
            print(current.data, end="\t")
            if current.left:
                Q.append(current.left)
            if current.right:
                Q.append(current.right)
            count+=1
        print(" ")

if __name__=="__main__":
    list =[10,20,5,7,13,8,15,28,18,25,35,40]
    tree = BinaryTree()
    for item in list:
        insertion(tree,item)
    Display(tree)