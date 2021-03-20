import BinaryTree
import BST_to_array_BFS
def RightSideView(root):
    if not root:
        return []
    q = [root]
    result = []
    while len(q):
        temp = []
        l = len(q)
        count = 0
        while count<l:
            current = q.pop(0)
            temp.append(current.data)
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)
            count+=1
        result.append(temp.pop())
    return result

if __name__=="__main__":
    list = [7,5,2,6,4,3,8,9]
    tree= BinaryTree.BinaryTree()
    for item in list:
        BinaryTree.InsertNode(tree,item)
    result = BST_to_array_BFS.BST_BFS(tree)
    print(result)
    result = RightSideView(tree)
    print(result)




