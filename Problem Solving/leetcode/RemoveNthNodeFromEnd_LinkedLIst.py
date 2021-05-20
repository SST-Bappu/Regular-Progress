class ListNode:
    def __init__(self,value=None):
        self.val = value
        self.next = None
def insertInList(head,value):
    if head.val==None:
        head.val = value
        return
    while head.next:
        head = head.next
    head.next = ListNode(value)
def displayList(head):
    while head:
        print(head.val, end="-->")
        head = head.next
def CountNode(head):
    count = 0
    while head:
        count+=1
        head = head.next
    return count
def RemoveNth(head,n):
    nodes = CountNode(head)
    target = (nodes - n)
    if target==0 and nodes==1:
        return None
    if target==0:
        return head.next
    cur = head
    target-=1
    while target>0:
        cur = cur.next
        target-=1
    cur.next = cur.next.next
    return head
def RemoveNth_optimized(head,n):
    fast = slow = head
    while n:
        fast = fast.next
        n-=1
    if not fast:
        return head.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return head



if __name__=="__main__":
    list = [1,2,3,4,5]
    head = ListNode()
    for item in list:
        insertInList(head,item)
    displayList(head)
    print("")
    head = RemoveNth_optimized(head,2)
    displayList(head)