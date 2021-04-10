from BinaryTree_parentLink import *
def hasPathSum(root, target):
    if not root:
        return False
    return FindPathSum(root,target)
def FindPathSum(root,target,sum=0):
    if not root.right and not root.left:
        return sum+root.data == target
    elif not root.left:
        return FindPathSum(root.right,target,sum+root.data)
    elif not root.right:
        return FindPathSum(root.left,target,sum+root.data)
    else:
        return FindPathSum(root.left,target,sum+root.data) or FindPathSum(root.right,target,sum+root.data)

if __name__=="__main__":
    list =[5,4,8,11,None,13,4,7,2,None,None,None,1]
    tree = BinaryTree()
    for item in list:
        insertion(tree,item)
    Display(tree)
    print(hasPathSum(tree,27))