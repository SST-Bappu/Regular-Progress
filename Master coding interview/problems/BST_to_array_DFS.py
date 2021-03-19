def MaximumDepth(Head):
    if Head == None:
        return 0
    return 1+max(MaximumDepth(Head.left),MaximumDepth(Head.right))
def BST_DFS(Head):
    if Head == None:
        return
    h = MaximumDepth(Head)
    for i in range(1, h + 1):
        
