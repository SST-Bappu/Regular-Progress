class LinkedList:
    def __init__(self,data = 0):
        self.data = data
        self.next = None
def FindIntersection(Node1,Node2):
    list = Node1
    L1 = 0
    L2 = 0
    tail1=None
    tail2 = None
    while(list):
        L1+=1
        tail1 = list
        list = list.next
    list = Node2
    while(list):
        L2+=1
        tail2 = list
        list = list.next
    if tail1 != tail2:
        return None
    Dif = abs(L1-L2)
    if L1>L2:
        list1 = Node1
        list2 = Node2
    else:
        list1 = Node2
        list2 = Node1
    while(Dif):
        list1 = list1.next
        Dif-=1
    while(list1 and list2):
        if list1==list2:
            return list1
        list1 = list1.next
        list2 = list2.next

if __name__=="__main__":
    list1 = [1,2,3]
    list2 = [5]
    list3 = [4,5,6]
    node1 = LinkedList(list1[0])
    node2 = LinkedList(list2[0])
    node3 =LinkedList(list3[0])
    node2.next = node3
    current = node1
    for i in range(1,len(list1)):
        current.next= LinkedList(list1[i])
        current = current.next
    current.next = node3
    current = node3
    for i in range(1,len(list3)):
        current.next = LinkedList(list3[i])
        current = current.next
    result = FindIntersection(node1,node2)
    if result:
        print(f"Intersecting point is ={result.data}")
    else:
        print("There is no Intersecting Point")
