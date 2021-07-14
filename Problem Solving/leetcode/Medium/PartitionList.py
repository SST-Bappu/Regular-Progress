class LinkedList():
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
def PartitionList(head,x):
    cur = head
    last = None
    while cur and cur.data<x:
        last = cur
        cur = cur.next
    if not cur:
        return head
    point = cur
    if not last:
        while cur:
            if cur.data<x:
                temp = cur.next
                cur.next = head
                last = head = cur
                prev.next = temp
                cur = temp
                break
            prev = cur
            cur = cur.next

    while cur:
        if cur.data<x:
            last.next = cur
            temp = cur.next
            last = last.next
            last.next = point

            prev.next = temp
            cur = temp
        else:
            prev = cur
            cur = cur.next
    return head

def Display(head):
    while head:
        print(head.data,end="-->")
        head = head.next

if __name__=="__main__":
    list = [3,1,2]
    head = LinkedList()
    cur = head
    for item in list:
        cur.next = LinkedList(item)
        cur = cur.next
    head = head.next
    head = PartitionList(head,3)
    Display(head)
