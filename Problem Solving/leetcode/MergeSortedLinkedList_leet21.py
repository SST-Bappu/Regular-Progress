class ListNode:
    def __init__(self, value=None):
        self.val = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self, value):
        if self.head==None:
            self.head = ListNode(value)
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = ListNode(value)
    def displayList(self):
        cur = self.head
        while cur:
            print(cur.val, end="-->")
            cur = cur.next

def MergeList(list1,list2):
    listMerged = LinkedList()
    while list1 and list2:
        if list1.val<list2.val:
            listMerged.insert(list1.val)
            list1 = list1.next
        else:
            listMerged.insert(list2.val)
            list2 = list2.next
    while list1:
        listMerged.insert(list1.val)
        list1 = list1.next
    while list2:
        listMerged.insert(list2.val)
    return listMerged
if __name__=="__main__":
    list1 = [1,2,4]
    list2 = [1,3,4]
    head1 = LinkedList()
    head2 = LinkedList()
    for item in list1:
        head1.insert(item)
    for item in list2:
        head2.insert(item)
    head = MergeList(head1.head,head2.head)
    head.displayList()