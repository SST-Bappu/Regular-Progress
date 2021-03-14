class node:
    def __init__(self,Data):
        self.data=Data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head=None
    def insert(self,newNode):
        if self.head is None:
            self.head=newNode
        else:
            currentNode=self.head
            while True:
                if currentNode.next==None:
                    break
                currentNode=currentNode.next
            currentNode.next=newNode
    def insert_at_specific(self,newNode,position):
        currentNode=self.head
        if position<=0:
            print("Invalid Position...!")
            return
        if position>0:
            self.head=newNode
            newNode.next=currentNode
            return
        for i in range(1,position-1):
            currentNode=currentNode.next
            if currentNode.next is None:
                print(f"You have only {i+1} nodes, New Node will be added as Last Node")
                currentNode.next = newNode
                return

        nextNode=currentNode.next
        currentNode.next=newNode
        newNode.next = nextNode
    def delete_node(self,position):
        currentNode=self.head
        prevNode = None
        currentPosition=1

        while True:
            if currentPosition==position:
                if prevNode is None:
                    self.head = currentNode.next
                    return
                else:
                    prevNode.next = currentNode.next
                    break
            prevNode=currentNode
            currentNode=currentNode.next
            currentPosition+=1


    def printList(self):
        currentNode=self.head
        print("The List is ->")
        while currentNode:
            print(currentNode.data)
            currentNode=currentNode.next

if __name__=="__main__":
    Node=node("Rahim")
    Llist=LinkedList()
    Llist.insert(Node)
    Node=node("Karim")
    Llist.insert(Node)
    Node=node("Kamal")
    Llist.insert(Node)
    Llist.printList()
    Node=node("John")
    Llist.insert_at_specific(Node,2)
    Llist.printList()
    Llist.delete_node(2)
    Llist.printList()