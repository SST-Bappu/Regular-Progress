import sys
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
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
