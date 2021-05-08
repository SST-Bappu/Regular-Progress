import sys
from queue import PriorityQueue
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def DisplayList(head):
    while head:
        print(head.val,end="-->")
        head = head.next
def MergeKsortedLists(lists):
    listMerged = None
    cur = None
    check = True
    while check:
        value = sys.maxsize
        i = 0
        check = False
        while i < len(lists):
            if lists[i] and lists[i].val < value:
                node = i
                value = lists[i].val
                check = True
            if not lists[i]:
                lists.pop(i)
                if check and i<node:
                    node-=1
            i += 1
        if check:
            if not cur:
                cur = ListNode(lists[node].val)
                listMerged = cur
                lists[node] = lists[node].next
            else:
                cur.next = ListNode(lists[node].val)
                cur = cur.next
                lists[node] = lists[node].next
    return listMerged
def MergeLinkedLists_optimized(lists): #Using Priority Queue
    head = cur = ListNode()
    Q = PriorityQueue()
    count = 0
    for node in lists:
        if node:
            Q.put((node.val,count,node))
            count+=1
    while not Q.empty():
        tuple = Q.get()
        value = tuple[0]
        cur.next = ListNode(value)
        cur = cur.next
        node = tuple[2].next
        if node:
            Q.put((node.val,count,node))
            count+=1
    return head.next

def MergeLists_DQ(lists): #Using Divide and Conquer Method
    if len(lists)==0:
        return None
    if len(lists)==1:
        return lists[0]
    mid = len(lists)//2
    l,r = MergeLists_DQ(lists[:mid]),MergeLists_DQ(lists[mid:])
    return merge(l,r)
def merge(left,right):
    cur = head = ListNode()
    while left and right:
        if left.val<right.val:
            cur.next = ListNode(left.val)
            cur = cur.next
            left = left.next
        else:
            cur.next = ListNode(right.val)
            cur = cur.next
            right = right.next
    while left:
        cur.next = ListNode(left.val)
        cur = cur.next
        left = left.next
    while right:
        cur.next = ListNode(right.val)
        cur = cur.next
        right = right.next
    return head.next


if __name__=="__main__":
    nums = [[1,4,5],[1,3,4],[2,6]]
    list1 = cur = ListNode()
    for item in nums[0]:
        cur.next = ListNode(item)
        cur = cur.next
    list1 = list1.next
    list2 = cur = ListNode()
    for item in nums[1]:
        cur.next = ListNode(item)
        cur = cur.next
    list2 = list2.next
    list3 = cur = ListNode()
    for item in nums[2]:
        cur.next = ListNode(item)
        cur = cur.next
    list3 = list3.next
    lists = [list1,list2,list3]
    head = MergeLists_DQ(lists)
    DisplayList(head)
