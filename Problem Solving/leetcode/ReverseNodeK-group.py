class listNode:
    def __init__(self,data=0,next=None):
        self.data = data
        self.next = next
def display(head):
    while head:
        print(head.data,end="-->")
        head = head.next
def ReverseNode(head,n):
    if n==1:
        return head
    cur = head
    list = []
    chk = True
    keep = None
    while cur:
        list.append(cur)
        if len(list) == n:
            tmp = list[n-1].next
            for j in range(n-1,0,-1):
                list[j].next = list[j-1]
            list[0].next = tmp
            if keep:
                keep.next = list[n-1]
            keep = list[0]
            if chk:
                head = list[n-1]
                chk = False
            list.clear()
            cur = tmp
        else:
            cur = cur.next
    return head
if __name__=="__main__":
    list = [1,2,3,4,5,6]
    head = cur = listNode()
    for item in list:
        cur.next = listNode(item)
        cur = cur.next
    display(head.next)
    print("")
    head = ReverseNode(head.next,1)
    display(head)




