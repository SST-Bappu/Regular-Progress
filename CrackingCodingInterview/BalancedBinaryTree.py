import BinaryTree
def checkBalance(root):
    if not root:
        return True
    if abs(depth(root.left)-depth(root.right))>1:
        return False
    else:
        return checkBalance(root.left) and checkBalance(root.right)
def depth(root):
    if not root:
        return 0
    return 1+max(depth(root.left),depth(root.right))

if __name__=="__main__":
    list = [8,10,12,15,16,3]
    #list=[5, 8, 7, 6, 3, 4, 2, 10, 2]
    Head = BinaryTree.BinaryTree()
    i = 0
    while (i < len(list)):
        BinaryTree.InsertNode(Head, list[i])
        i += 1
    BinaryTree.InOrderTraversal(Head)
    print("")
    print(checkBalance(Head))