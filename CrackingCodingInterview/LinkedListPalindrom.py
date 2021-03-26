class LinkedList:
    def __init__(self,data=0):
        self.data = data
        self.next = None
def ReverseList(Head):
    prev = None
    while(Head):
        node = LinkedList(Head.data)
        node.next = prev
        prev = node
        Head = Head.next
    return prev
def Palindrome(head1,head2):
    fast = head2.next
    while(fast):
        if head1.data != head2.data:
            return False
        head1=head1.next
        head2=head2.next
        fast = fast.next.next
    return True
def Palindrome_Stack(head): #Optimized
#Iterative process, no need to reverse the list. We push the first half and then check the second half
    list=[]
    fast = head
    while(fast and fast.next):
        list.append(head.data)
        head=head.next
        fast=fast.next.next
    if fast!=None:
        .304
    
        head=head.next
    while(head):
        if head.data!=list.pop():
            return False
        head = head.next
    return True
if __name__=="__main__":
    list = [1,2,1,2,1]
    node = LinkedList(list[0])
    current = node
    for i in range(1,len(list)):
        current.next = LinkedList(list[i])
        current = current.next
    nodeR = ReverseList(node)
    current = nodeR
    while(current):
        print(current.data,end="->")
        current = current.next
    print("")
    print(Palindrome_Stack(node))