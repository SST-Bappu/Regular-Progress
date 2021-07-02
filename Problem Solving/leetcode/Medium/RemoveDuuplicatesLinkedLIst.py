class LinkedList:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

def RemoveDuplicates(head):
    cur = head
    head = LinkedList(0,head)
    prev = head
    while cur:
        if cur.next and cur.data == cur.next.data:
            while cur.next and cur.data == cur.next.data:
                cur = cur.next
            prev.next = cur.next
        else:
            prev = prev.next
        cur = cur.next
    return head.next

def Display(head):
    while head:
        print(head.data,end = "-->")
        head = head.next
if __name__=="__main__":
    list = [1,1,2,3,3,4,4,5,5]
    head = LinkedList()
    cur = head
    for num in list:
        cur.next = LinkedList(num)
        cur = cur.next
    Display(head.next)
    print("")
    head = RemoveDuplicates(head.next)
    Display(head)