from collections import deque
from BinaryTree_parentLink import *
def FindNodes(tree,data1,data2,result=[]):
    if not tree:
        return result
    if tree.data == data1 or tree.data == data2:
        result.append(tree)
        if len(result)==2:
            return result
    FindNodes(tree.left,data1,data2,result)
    FindNodes(tree.right,data1,data2,result)
    return result
def CommonAnchestor(p,q):
    diff = Depth(p)-Depth(q)
    first = p if diff>0 else q
    second = q if diff>0 else p
    count = abs(diff)
    while count:
        first = first.parent
        count-=1
    while first != second:
        first = first.parent
        second = second.parent
    return first

def Depth(node):
    count = 0
    while node:
        node = node.parent
        count+=1
    return count
if __name__=="__main__":
    list =[10,20,5,7,13,8,15,28,18,25,35,40]
    tree =BinaryTree()
    for item in list:
        insertion(tree,item)
    Display(tree)
    result = FindNodes(tree,8,15)
    parent = CommonAnchestor(result[0],result[1])
    print("This is the first common anchestor between the nodes - ", parent.data)
