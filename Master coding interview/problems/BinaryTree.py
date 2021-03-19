class BinaryTree:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None
def InsertNode(head,data):
    if head.data==None:
        head.data = data
        print("Data Inserted = ",data)
        return
    if data >= head.data:
        if not head.right:
            head.right = BinaryTree()
        InsertNode(head.right,data)
    else:
        if not head.left:
            head.left=BinaryTree()
        InsertNode(head.left,data)
def MaximumDepth(Head):
    if Head == None:
        return 0
    return 1+max(MaximumDepth(Head.left),MaximumDepth(Head.right))
def DisplayBinaryTree(head):
    if head==None:
        return
    print(head.data)
    DisplayBinaryTree(head.left)
    DisplayBinaryTree(head.right)
if __name__=="__main__":
    list = [5,8,7,6,3,4,2,10]
    Head = BinaryTree()
    i=0
    while(i<len(list)):
        InsertNode(Head,list[i])
        i+=1
    DisplayBinaryTree(Head)
    print("Maximum Depth is = ",MaximumDepth(Head))

