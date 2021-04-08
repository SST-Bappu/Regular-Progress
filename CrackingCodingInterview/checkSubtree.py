from BinaryTree_parentLink import *
def checkSubtree(T1,T2):
    Tree_string1 = preOrder(T1)
    Tree_string2 = preOrder(T2)
    print(Tree_string1)
    print(Tree_string2)
    return True if Tree_string2 in Tree_string1 else False

def preOrder(tree,string=""):
    if not tree:
        return string
    string+=str(tree.data)
    string+=preOrder(tree.left)
    string+=preOrder(tree.right)
    return string


if __name__=="__main__":
    list =[10,20,5,7,13,8,15,28,18,25,35,40]
    tree =BinaryTree()
    for item in list:
        insertion(tree,item)
    list2 = [13,25,35]
    tree2 = BinaryTree()
    for item in list2:
        insertion(tree2,item)
    #Display(tree)
    #Display(tree2)
    print(checkSubtree(tree,tree2))

