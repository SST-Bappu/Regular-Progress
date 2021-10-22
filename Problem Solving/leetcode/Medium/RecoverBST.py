class treeNode:
    def __init__(self,val=None,left=None,right=None):
        self.left = left
        self.right = right
        self.val = val

def constructBST(root,val):
    if root.val==None:
        root.val = val
        return
    if val>root.val:
        if not root.right:
            root.right = treeNode()
        constructBST(root.right,val)
    else:
        if not root.left:
            root.left = treeNode()
        constructBST(root.left,val)



def traverseBST(root,list):
    if not root:
        return
    traverseBST(root.left,list)
    list.append(root)
    traverseBST(root.right,list)
if __name__=="__main__":
    # num = [8,5,10,6,3,9,15]
    # root = treeNode()
    # for i in num:
    #     constructBST(root,i)
    # traverseBST(root)
    root = treeNode(1)
    root.left = treeNode(3)
    temp = root.left
    temp.right = treeNode(2)
    list = []
    traverseBST(root,list)
    for node in list:
        print(node.val,end="->")
    print()
    sortedlist = sorted(i.val for i in list)
    for i in range(len(list)):
        list[i].val = sortedlist[i]
    for node in list:
        print(node.val,end="->")
