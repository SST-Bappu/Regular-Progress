class LinkedList:
    def __init__(self,data):
        self.data = data
        self.next = None
def Partition(head,data):
    current = head
    node = head
    prev = None
    while(True):
        if current.data==data:
            break
        prev = current
        current = current.next
    prevE=None
    chk = False
    while node:
        if node == current:
            chk = True
        if node.data>data and not chk:
            if not prevE:
                head = node.next
                node.next = current.next
                current.next = node
                node = head
            else:
                prevE.next = node.next
                node.next = current.next
                current.next = node
                node = prevE.next
        elif node.data<=data and node!=current and chk:
            prevE.next=node.next
            prev.next = node
            node.next = current
            prev = node
            node = prevE.next
        else:
            prevE = node
            node = node.next
    return head

if __name__=="__main__":
    list=[6,3,8,4,5,2,1]
    node = LinkedList(list[0])
    current = node
    for i in range(1,len(list)):
        current.next=LinkedList(list[i])
        current=current.next
    current = Partition(node,5)
    while(current):
        print(current.data,end="->")
        current=current.next
