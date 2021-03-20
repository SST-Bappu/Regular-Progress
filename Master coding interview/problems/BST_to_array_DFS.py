import BinaryTree
def BST_DFS(root):
    if not root:
        return []
    result = []
    q = [root]
    while len(q):
        l = len(q)
        count = 0
        Data_every_level = []
        while count<l:
            current = q.pop(0)
            Data_every_level.append(current.data)
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)
            count+=1
        result.append(Data_every_level)
    return result
if __name__=="__main__":
    list = [5,8,7,6,3,4,2,10,2]
    Head = BinaryTree.BinaryTree()
    i=0
    while(i<len(list)):
        BinaryTree.InsertNode(Head,list[i])
        i+=1
    result = BST_DFS(Head)
    print(result)
