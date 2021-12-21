class LinkedList:
    def __init__(self,data=None):
        self.data = data
        self.next = None
def DeleteMiddle(head):
    prev = None
    slow = head
    fast = head
    while(fast and fast.next!=None):
        prev = slow
        slow = slow.next
        fast = fast.next.next
    if prev!=None :
        prev.next = slow.next
def DeleteDups(head):
    HashTable=dict()
    prev=None
    while(head):
        if HashTable.get(head.data):
            prev.next = head.next
        else:
            HashTable.update({head.data:head.data})
            prev = head
        head=head.next
def DeleteDups_NoAlternateBuffer(head):
    HashTable=dict({head.data:head.data})
    while(head.next):
        if HashTable.get(head.next.data):
            head.next = head.next.next
        else:
            HashTable.update({head.next.data:head.next.data})
            head=head.next

if __name__=="__main__":
    arr=[1,2,2,2,3,1,4,3,2,5,7,6,4]
    node = LinkedList(arr[0])
    newNode = node
    for i in range(len(arr)-1):
        newNode.next=LinkedList(arr[i+1])
        newNode=newNode.next
    DeleteDups_NoAlternateBuffer(node)
    newNode = node
    while (newNode):
        print(newNode.data, end="->")
        newNode = newNode.next
    print()
    DeleteMiddle(node)
    newNode = node
    while (newNode):
        print(newNode.data, end="->")
        newNode = newNode.next