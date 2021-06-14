class LinkedList:
    def __init__(self,data=None):
        self.data = data
        self.next = None
def RotateList(head,k):
    if not head or not head.next:
        return head
    n = 1
    cur = head
    while cur.next:
        cur = cur.next
        n+=1
    if k%n==0:
        return head
    last = head
    for i in range(n-k%n-1):
        last = last.next
    newHead = last.next
    cur.next = head
    last.next = None
    return newHead
def Display(head):
    while head:
        print(head.data,end="-->>")
        head = head.next

if __name__=="__main__":
    head = LinkedList()
    cur = head
    for i in range(3):
        cur.next = (LinkedList(i))
        cur = cur.next
    head = RotateList(head.next,5)
    Display(head)