import timeit
def MinimumCost(cost):
    n= len(cost)
    cost.append(0)
    return CalMinCost(cost,n)
def CalMinCost(cost,n):
    if n==0 or n==1:
        return cost[n]
    return cost[n]+min(CalMinCost(cost,n-1),CalMinCost(cost,n-2))
#Dynamic Programming (Top Down Approach)
def MinimumCost_optimized(cost): #Here I'm introducing Dynamic Programming for the very first time
    n= len(cost)                #Here I basically applied Top Down Approach
    cost.append(0)
    memo = {}
    return MinCost(cost,n,memo)
def MinCost(cost,n,memo):
    if n==0 or n==1:
        return cost[n]
    if memo.get(n):
        return memo[n]
    memo[n] = cost[n]+min(MinCost(cost,n-1,memo),MinCost(cost,n-2,memo))
    return memo[n]

#Dynamic Programming Bottom up approach
def MinimuCost_BottomUp(cost): #Let's apply Bottom  up approach in the same problem
    n = len(cost)
    dp1 = cost[0]
    dp2 = cost[1]
    i=2
    while i<n:
       current = cost[i]+min(dp1,dp2)
       dp1 = dp2
       dp2 = current
       i+=1
    return min(dp1,dp2)
if __name__=="__main__":
    cost = [20,15,30,5]
    start = timeit.default_timer()
    print(MinimumCost(cost))
    stop = timeit.default_timer()
    print(stop-start)
    start = timeit.default_timer()
    print(MinimumCost_optimized(cost))
    stop = timeit.default_timer()
    print(stop-start)
    start = timeit.default_timer()
    print(MinimuCost_BottomUp(cost))
    print(timeit.default_timer()-start)