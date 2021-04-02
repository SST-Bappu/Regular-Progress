import BinaryTree
def BSTMinimalDepth(root, array, start, end):
    if start>end:
        return
    mid = (start+end)//2
    BinaryTree.InsertNode(root,array[mid])
    BSTMinimalDepth(root,array,start,mid-1)
    BSTMinimalDepth(root,array,mid+1,end)

if __name__=="__main__":
    root = BinaryTree.BinaryTree()
    SortedArray = [2,4,5,8,10,15,20,35,50,60,65,70,75,80,90]
    BSTMinimalDepth(root,SortedArray,0,len(SortedArray)-1)
    print(BinaryTree.MaximumDepth(root))
    BinaryTree.InOrderTraversal(root)