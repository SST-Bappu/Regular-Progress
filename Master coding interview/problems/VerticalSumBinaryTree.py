from BinaryTree import *
def VerticalSum(root,sum={}, level = 0):
    if not root:
        return sum
    if sum.get(level):
        sum[level]+=root.data
    else:
        sum[level] = root.data

    VerticalSum(root.right,sum,level+1)
    VerticalSum(root.left,sum,level-1)
    return sum

if __name__=="__main__":
    list = [5, 8, 7, 6, 3, 4, 2, 10]
    Head = BinaryTree()
    i = 0
    while (i < len(list)):
        InsertNode(Head, list[i])
        i += 1
    InOrderTraversal(Head)
    print("")
    print(VerticalSum(Head))