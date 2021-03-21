import BinaryTree
import BST_to_array_BFS
def RightSideView(root): #Using Breadth First Search
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
def RightSideView_DFS(root,result=[],Level=1):
    if not root:
        return
    if Level>len(result):
        result.append(root.data)
    RightSideView_DFS(root.right,result,Level+1)
    RightSideView_DFS(root.left,result,Level+1)
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
    print(RightSideView_DFS(tree))




