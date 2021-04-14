def TripleSteps(n):
    memo = [None for i in range(n+1)]
    return CountSteps(memo,n)
def CountSteps(memo,n): #Top Down approach
    if n<0:
        return 0
    if n==0:
        return 1
    if memo[n]:
        return memo[n]
    memo[n] = CountSteps(memo,n-1)+CountSteps(memo,n-2)+CountSteps(memo,n-3)
    return memo[n]

def CountSteps_Bottomup(n):
    memo1 = 1
    memo2 = 1
    memo3 = 2
    i = 3
    while i<=n:
        current = memo1+memo2+memo3
        memo1 = memo2
        memo2  = memo3
        memo3 = current
        i+=1
    return memo3

if __name__=="__main__":
    n=8
    print(TripleSteps(n))
    print(CountSteps_Bottomup(n))