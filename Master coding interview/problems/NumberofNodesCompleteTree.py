import BinaryTree
import Heap_LinkedList_Implementation
import BST_to_array_BFS
import math
def NumberofNodes(root):
    height = BinaryTree.MaximumDepth(root)-1
    UpperCount = pow(2,height)
    left = 0
    right = UpperCount-1
    while left<right:
        IdxToFind = math.ceil((left+right)/2)
        if not Exists(root,IdxToFind,height):
            left = IdxToFind
        else:
            right = IdxToFind-1
    return UpperCount+left
def Exists(root,IdxToFind,height):
    left = 0
    right = pow(2,height)-1
    count = 0
    while count<height:
        mid = math.ceil((left+right)/2)
        if mid<=IdxToFind:
            root = root.right
            left = mid
        else:
            root = root.left
            right = mid-1
        count+=1
    return not root
def FindNumberOfNodes(root): #Less Optimized
    height = BinaryTree.MaximumDepth(root)
    return pow(2,height-1)+LevelTraverse(root,height-1)-1
def LevelTraverse(root,height):
    if not root:
        return 0
    count = 0
    if height==1:
        if root.left:
            count+=1
        if root.right:
            count+=1
        return count
    else:
        count+=LevelTraverse(root.left,height-1)
        count+=LevelTraverse(root.right,height-1)
    return count
if __name__=="__main__":
    list =[10, 30, 20, 35, 40, 32, 25, 5, 2, 8, 12, 4, 50]
    root = BinaryTree.BinaryTree()
    for item in list:
        Heap_LinkedList_Implementation.InsertMinHeap(root,item)
    result = BST_to_array_BFS.BST_BFS(root)
    print(result)
    print(NumberofNodes(root))
    print(FindNumberOfNodes(root))

