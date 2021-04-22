import copy
def sumSubsets(weights,m):
    return subsets(weights,m,len(weights)-1)
def subsets(weights,total,index):
   if total==0:
       return 1
   if total<0:
       return 0
   if index<0:
       return 0
   if total<weights[index]:
       return subsets(weights,total,index-1)
   else:
       return subsets(weights,total-weights[index],index-1)+subsets(weights,total,index-1)
if __name__=="__main__":
    list = [5,10,15,20]
    print(sumSubsets(list,50))