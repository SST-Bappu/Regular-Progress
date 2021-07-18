class TreeNode:
    def __init__(self,data=None):
        self.val = data
        self.left = None
        self.right = None
def CreateBinaryTree(root,data):
    if not root.val:
        root.val = data
        return
    if data>root.val:
        if not root.right:
            root.right = TreeNode()
        CreateBinaryTree(root.right,data)
    else:
        if not root.left:
            root.left = TreeNode()
        CreateBinaryTree(root.left,data)

def inorderTraversal(root,result = []):
    if not root:
        return
    inorderTraversal(root.left,result)
    result.append(root.val)
    inorderTraversal(root.right,result)
    return result


if __name__=="__main__":
    nums = [10,5,15,20,12,3,8]
    root = TreeNode()
    for item in nums:
        CreateBinaryTree(root,item)
    result = inorderTraversal(root)
    print(result)