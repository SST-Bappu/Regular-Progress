from BinaryTree_parentLink import *
def pathsWithSum(Tree,target,sum=0,count=0):
    if not Tree:
        return count
    sum+=Tree.data
    if sum==target:
        count+=1
        sum = 0
        #print(Tree.data)
    elif sum>target:
        sum=0
    count += pathsWithSum(Tree.left,target,sum)
    count += pathsWithSum(Tree.right,target,sum)
    return count

if __name__=="__main__":
    list =[10,5,-3,3,2,11,3,-2,-5,1]
    tree = BinaryTree()
    for item in list:
        insertion(tree,item)
    Display(tree)
    print(pathsWithSum(tree,8))