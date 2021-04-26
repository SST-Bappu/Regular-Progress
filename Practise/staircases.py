def Staircases(n):
    memo={}
    return ways(memo,n)
def ways(memo,n):
    if memo.get(n):
        return memo[n]
    if n<0:
        return 0
    if n==0:
        return 1
    memo[n] = Staircases(n-1)+Staircases(n-2)+Staircases(n-3)
    return memo[n]
if __name__=="__main__":
    print(Staircases(6))