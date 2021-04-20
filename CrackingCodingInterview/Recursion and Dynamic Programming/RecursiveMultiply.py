import timeit
def RecursiveMultiply(n,m):
    if m==0:
        return 0
    if m==1:
        return n
    return n+RecursiveMultiply(n,m-1)
#Using Dynamic Programming and more optimized way
def multiply(n,m):
    bigger = n if n>m else m
    smaller = n if n<m else m
    memo = [None for i in range(smaller+1)]
    return RecurseMultiplyOptimized(memo, smaller, bigger)

def RecurseMultiplyOptimized(memo,smaller,bigger):
    if smaller == 0:
        return 0
    if smaller == 1:
        return bigger
    if memo[smaller]:
        return memo[smaller]
    s = smaller >> 1
    side1 = RecurseMultiplyOptimized(memo,s,bigger)
    side2 = side1
    if smaller%2==1:
        side2 = RecurseMultiplyOptimized(memo,smaller-s,bigger)
    memo[smaller] = side1+side2
    return memo[smaller]
if __name__=="__main__":
    start = timeit.default_timer()
    print(RecursiveMultiply(20,17))
    print(timeit.default_timer()-start)
    start = timeit.default_timer()
    print(multiply(20,17))
    print(timeit.default_timer()-start)