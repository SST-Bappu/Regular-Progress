from collections import deque
import BSTwithMinimalDepth
import BinaryTree
class LinkedList:
    def __init__(self,data=None):
        self.data = data
        self.next = None

def ListOfDepths(root): #Using Breadth First Search
    if not root:
        return
    Q = deque()
    linkedlists = []
    Q.append(root)
    while len(Q):
        n = len(Q)
        count = 0
        Head = LinkedList()
        linkedlists.append(Head)
        while(count<n):
            current = Q.popleft()
            if current.left:
                Q.append(current.left)
            if current.right:
                Q.append(current.right)
            Head.data = current.data
            Head.next= LinkedList()
            Head = Head.next
            count+=1
    return linkedlists
def ListOfDepths_DFS(root,linkedLists,level=0): #Using Depth First Search
    if not root:
        return
    if level == len(linkedLists):
        linkedLists.append(LinkedList(root.data))
    else:
        LinkedList_insert(linkedLists[level],root.data)
    ListOfDepths_DFS(root.left,linkedLists,level+1)
    ListOfDepths_DFS(root.right,linkedLists,level+1)
def TraverseLinkedLists(Head):
    if not Head or not Head.data:
        return
    print(Head.data, end="->")
    TraverseLinkedLists(Head.next)
def LinkedList_insert(Head,data):
    if not Head.next:
        Head.next = LinkedList(data)
        return
    LinkedList_insert(Head.next,data)

if __name__=="__main__":
    root = BinaryTree.BinaryTree()
    SortedArray = [2, 4, 5, 8, 10, 15, 20, 35, 50, 60, 65, 70, 75, 80, 90]
    BSTwithMinimalDepth.BSTMinimalDepth(root, SortedArray, 0, len(SortedArray) - 1)
    print(BinaryTree.MaximumDepth(root))
    BinaryTree.InOrderTraversal(root)
    print(" ")
    lists = ListOfDepths(root)
    for head in lists:
        TraverseLinkedLists(head)
        print(" ")
    linkedLists = []
    ListOfDepths_DFS(root,linkedLists)
    for head in linkedLists:
        TraverseLinkedLists(head)
        print("")
