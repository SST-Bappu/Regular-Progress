class ListNode:
    def __init__(self,data=None):
        self.data = data
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def insert_node(self,item):
        if self.head ==None:
            self.head = ListNode(item)
            return
        curNode = self.head
        while(curNode.next!=None):
            curNode = curNode.next
        NewNode = ListNode(item)
        curNode.next = NewNode
        NewNode.prev = curNode
def sortedInsert(head,data):
    if head is None:
        head = ListNode(data)
        return head
    curNode = head
    prev = None
    while(curNode):
        if curNode.data>=data:
            NewNode = ListNode(data)
            prev.next = NewNode
            NewNode.prev = prev
            NewNode.next = curNode
            curNode.prev = NewNode
            return head
        else:
            prev = curNode
            curNode = curNode.next

    prev.next = ListNode(data)
    curNode = prev.next
    curNode.prev = prev
    return head

def print_doubly_linked_list(head):
    curNode =head
    while(curNode):
        print(curNode.data)
        curNode = curNode.next
if __name__=="__main__":
    list = DoublyLinkedList()
    t = 1#int(input("t = "))
    while(t):
        n = 0#int(input("n = "))
        print("Node Data Values = ")
        while(n):
            item=int(input())
            list.insert_node(item)
            n-=1
        data = 15#int(input("Data = "))
        list1=sortedInsert(list.head,data)
        print_doubly_linked_list(list1)
        t-=1
