class LinkedList:
    def __init__(self,data=None):
        self.data = data
        self.next = None
def MergeLinkedList(list1,list2):
    List= LinkedList()
    NewList = List
    while list1 and list2:
        if list1.data<list2.data:
            NewList.data = list1.data
            list1 = list1.next
        else:
            NewList.data = list2.data
            list2 = list2.next
        NewList.next = LinkedList()
        NewList = NewList.next
    while list1:
        NewList.data = list1.data
        NewList.next = LinkedList()
        NewList = NewList.next
        list1 = list1.next
    while list2:
        NewList.data = list2.data
        NewList.next = LinkedList()
        NewList = NewList.next
        list2 = list2.next
    return List

def insertLinkedList(list,data):
    while list.next:
        list = list.next
    list.next = LinkedList(data)
def DisplayLinkedList(list):
    while list.next:
        print(list.data,end="->")
        list = list.next

if __name__=="__main__":
    l1 = [1,2,4]
    l2 = [1,3,4]
    list1 = LinkedList(l1[0])
    list2 = LinkedList(l2[0])
    i = 1
    while i<len(l1):
        insertLinkedList(list1,l1[i])
        i+=1
    i=1
    while i<len(l2):
        insertLinkedList(list2,l2[i])
        i+=1

    List = MergeLinkedList(list1,list2)
    DisplayLinkedList(List)


