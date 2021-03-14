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
    def Find_Merge_Point(self,head1,head2):

if __name__=="__main__":
    MainNode = None
    Node1 = None
    Node2 = None
    list1 = [50,60,70]
    list2 = [10,15,25]
    list3 = [1,3,4]
    t = 1#int(input("t = "))
    while(t):
        for index in list1:
            if MainNode is None:
                MainNode = DoublyLinkedList()
            MainNode.insert_node(index)
        for index in list2:
            if Node1 is None:
                Node1 = DoublyLinkedList()
            Node1.insert_node(index)
        for index in list3:
            if Node2 is None:
                Node2 = DoublyLinkedList
            Node2.insert_node(index)

        data = 15#int(input("Data = "))
        list1=sortedInsert(list.head,data)
        print_doubly_linked_list(list1)
        t-=1