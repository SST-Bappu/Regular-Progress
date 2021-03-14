import timeit
def solution2(n,arr):
    maxDist = 0
    lastSeen=None
    j=0
    m = len(arr)
    for i in range(n):
        if i in arr:
            dist = 0
            lastSeen = i
        elif lastSeen is not None:
            dist = i-lastSeen
            r = i+dist
            for k in range(i+1,r):
                if k in arr:
                    dist = k-i
                    break
        else:
            for k in range(i+1,n):
                if k in arr:
                    dist = k-i
                    break
        maxDist=max(maxDist,dist)
    return maxDist
def solution1(n,arr):
    arr.sort()
    maxDist = 0
    m = len(arr)
    j=0
    lastSeen = None
    for i in range(n):
        if i in arr:
            dist = 0
            lastSeen = i
            j+=1
        elif lastSeen is not None:
            if j<m:
                dist = min((i-lastSeen),(arr[j]-i))
            else:
                dist = i - lastSeen
        else:
            dist = abs(arr[j]-i)
        maxDist = max(dist,maxDist)
    return maxDist
def solution_optimized(n,arr):
    arr.sort()
    maxDist = max(arr[0],n-1-arr[-1])
    print(maxDist)
    for i in range(len(arr)-1):
        maxDist = max(maxDist,(arr[i+1]-arr[i])//2)
    return maxDist

if __name__=="__main__":
    list=[4,5,2,3]
    t1 = timeit.default_timer()
    print(solution1(6,list))
    t2 = timeit.default_timer()-t1
    print(t2)
    t1 = timeit.default_timer()
    print(solution2(6, list))
    t2 = timeit.default_timer() - t1
    print(t2)
    t1 = timeit.default_timer()
    print(solution_optimized(6,list))
    t2 = timeit.default_timer() - t1
    print(t2)




