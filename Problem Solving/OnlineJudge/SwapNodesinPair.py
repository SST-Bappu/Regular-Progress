class listNode:
    def __init__(self,data=0,next=None):
        self.data = data
        self.next = None

def SwapNodespair(head):
    cur = head
    chk = True
    left = None
    while cur:
        if cur.next:
            tmp = cur.next
            cur.next = tmp.next
            tmp.next = cur
            if chk:
                head = tmp
                chk = False
            if left:
                left.next = tmp
        left = cur
        cur = cur.next

    return head
def display(head):
    while head:
        print(head.data,end="-->")
        head = head.next

if __name__=="__main__":
    list = [1,2,3,4]
    head = cur = listNode()
    for item in list:
        cur.next = listNode(item)
        cur = cur.next
    display(head.next)
    head = SwapNodespair(head.next)
    print("")
    display(head)
