class treeNode:
    def __init__(self,val=None):
        self.val = val
        self.left = None
        self.right = None
def constructTree(list,val,i=0):
    while(list):
        root = list[i]
        if root.val==None:
            root.val = val
            return
        if not root.left:
            root.left = treeNode(val)
            return
        if not root.right:
            root.right = treeNode(val)
            return
        list.append(root.left)
        list.append(root.right)
        i+=1
def dfs1(root):
    if not root:
        return
    dfs(root.left)
    print(root.val,end="->>")
    dfs(root.right)
def isSymmetric(root):

    return dfs(root.left,root.right)

def dfs(rootL, rootR):
    if not rootL and not rootR:
        return True
    if not rootL or not rootR:
        return False
    if not rootL.left and rootR.right:
        return True
    if rootL.val != rootR.val:
        return False
    return dfs(rootL.left, rootR.right) and dfs(rootL.right, rootR.left)


if __name__=="__main__":
    list = [1,2,2,None,3,None,3]
    root = treeNode()
    nodes = [root]
    for item in list:
        constructTree(nodes,item)
    print(isSymmetric(root))
