class ListNode:
    def __init__(self,data=0):
        self.data=data
        self.next=None
class Solution:
    def addTwoNumbers(self,l1,l2,c=0):
        sum = l1.data + l2.data + c
        result = ListNode(sum%10)
        c = sum//10
        if l1.next!=None or l2.next!=None or c!=0:
            if l1.next==None:
                l1.next = ListNode()
            if l2.next==None:
                l2.next=ListNode()
            result.next = self.addTwoNumbers(l1.next,l2.next,c)
        return result


if __name__=="__main__":
    data = [2, 4, 3]
    data2 = [5, 6, 4]
    node = ListNode()
    node2 = ListNode()
    curNode = node
    for i in data:
        curNode.data = i
        curNode.next = ListNode()
        curNode=curNode.next
    curNode = node2
    for i in data2:
        curNode.data = i
        curNode.next = ListNode()
        curNode=curNode.next
    result = Solution()
    sum = result.addTwoNumbers(node,node2)
    while True:
        if sum.next == None:
            break
        print(sum.data, end="->")
        sum = sum.next
