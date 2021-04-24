import copy
def sumSubsets(weights,m):
    arrangements=[]
    result = subsets(weights,m,len(weights)-1,arrangements)
    print(arrangements)
    return result
def subsets(weights,total,index,arrangements,arr=[]):
   if total==0:
       arrangements.append(arr)
       return 1
   if total<0:
       return 0
   if index<0:
       return 0
   if total<weights[index]:
       return subsets(weights,total,index-1,arrangements, arr)
   else:
       new=copy.deepcopy(arr)
       new.append(weights[index])
       return subsets(weights,total-weights[index],index-1,arrangements,new)+subsets(weights,total,index-1,arrangements, arr)

def SumSubsets_dp(weights,m):
    memo ={}
    result= Subset_DP(weights,m,len(weights)-1,memo)
    return result
def Subset_DP(weights,total,index,memo,arr=[]):
    key = str(total)+':'+str(index)
    if memo.get(key):
        return memo[key]
    if total==0:
        return arr
    if total<0:
        return False
    if index<0:
        return False
    if total<weights[index]:
        result = Subset_DP(weights,total,index-1,memo,arr)
        if result:
            memo[key] = result
    else:
        new = copy.deepcopy(arr)
        new.append(weights[index])
        r1 = Subset_DP(weights,total-weights[index],index-1,memo,new)
        r2 = Subset_DP(weights,total,index-1,memo,copy.deepcopy(arr))
        memo[key] = []
        if r1:
            memo[key].append(r1)
        if r2:
            memo[key].append(r2)
    return memo[key]
if __name__=="__main__":
    #list = [2,4,5,6,10,15,20]
    list=[5,10,15,20]
    print(sumSubsets(list,30))
    print(SumSubsets_dp(list,30))