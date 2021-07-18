class ListNode:
    def __init__(self,val=None,next=None):
        self.val = val
        self.next = next
def ReverseLinkedList(head,left,right):
    i = 1
    cur = head
    keep = None
    stack = []
    while i<=right:
        if i+1==left:
            keep = cur
        if i>=left:
            stack.append(cur)
        cur = cur.next
        i+=1
    if left == 1:
        keep = stack.pop()
        head = keep
    while stack:
        keep.next = stack.pop()
        keep = keep.next
    keep.next = cur
    return head

def Display(head):
    while head:
        print(head.val,end="->>")
        head = head.next

if __name__=="__main__":
    head = cur = ListNode()
    nums = [5,6]
    for item in nums:
        cur.next = ListNode(item)
        cur = cur.next
    head = head.next
    head = ReverseLinkedList(head,1,2)
    Display(head)