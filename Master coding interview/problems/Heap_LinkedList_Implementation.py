#Linked List Implementation
import BinaryTree
import BST_to_array_DFS
def InsertMinHeap(root,data):
    if not root.data:
        root.data = data
        return
    q = [root]
    while len(q):
        l = len(q)
        count = 0
        while count<l:
            current = q.pop(0)
            if not current.left:
                current.left = BinaryTree.BinaryTree(data)
                return
            elif not current.right:
                current.right = BinaryTree.BinaryTree(data)
                return
            else:
                q.append(current.left)
                q.append(current.right)
            count+=1
def InsertMinHeap_optimized(root,data):
    if not root.data:
        root.data = data
        return
    q = [root]
    i=0
    cnt = 0
    while True:
        j = i+pow(2,cnt)
        count = 0
        while count<pow(2,cnt):
            value = j+count-pow(2,cnt)
            current = q[value]
            if not current.left:
                current.left = BinaryTree.BinaryTree(data)
                q.append(current.left)
                ReArrange(q,cnt+1)
                return
            else:
                q.append(current.left)
            if not current.right:
                current.right = BinaryTree.BinaryTree(data)
                q.append(current.right)
                ReArrange(q,cnt+1)
                return
            else:
                q.append(current.right)
            count+=1
        i+=pow(2,cnt)
        cnt+=1
def ReArrange(Q,Level):
    l = len(Q)
    while Level:
        current = Q[l - 1]
        root_idx = pow(2,Level-1)-1+(pow(2,Level)-(pow(2,Level+1)-l))//2
        root = Q[root_idx]
        if current.data<root.data:
            current.data, root.data = root.data, current.data
            Level-=1
            l = root_idx+1
        else:
            Q.clear()
            return
def Remove_from_Heap(root):
    level = BinaryTree.MaximumDepth(root)
    last = FindLast(root,level)
    if not last:
        root = None
    root.data = last.data
    After_Remove(root)
def After_Remove(root):
    if not root or (not root.left and not root.right):
        return
    if not root.left:
        root.data, root.right.data = root.right.data, root.data
        After_Remove(root.right)
    elif not root.right:
        root.data, root.left.data = root.left.data, root.data
        After_Remove(root.left)
    elif root.left.data<root.right.data:
        root.data,root.left.data = root.left.data, root.data
        After_Remove(root.left)
    else:
        root.data,root.right.data = root.right.data,root.data
        After_Remove(root.right)


def FindLast(root,level):
    if not root:
        return None
    if level==1 and root.left==None:
        return root
    right = FindLast(root.right,level-1)
    left = FindLast(root.left,level-1)
    return right if right else left

if __name__=="__main__":
    list = [10,30,20,35,40,32,25,5,2,8,12,4]
    root = BinaryTree.BinaryTree()
    i=0
    while(i<len(list)):
        InsertMinHeap_optimized(root,list[i])
        i+=1
    result = BST_to_array_DFS.BST_DFS(root)
    print(result)
    BinaryTree.PreOrderTraversal(root)
    print("")
    Remove_from_Heap(root)
    result = BST_to_array_DFS.BST_DFS(root)
    print(result)