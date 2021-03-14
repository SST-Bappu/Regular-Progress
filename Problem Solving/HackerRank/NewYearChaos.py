import timeit
def minimumBribes(q):
    n = len(q)-1
    bribes = 0
    while n>0:
        dif = 0
        if q[n-1]>q[n]:
            dif = q[n-1]-q[n]
        if dif>2:
            print("Too chaotic")
            return
        bribes += dif
        n-=1
    print(bribes)
def Solution3(q):
        n = len(q)
        bribes = 0
        for i in range(n):
            dif = 0
            if q[i]-(i+1)>2:
                print("Too chaotic")
                return
            for j in range(i + 1, n):
                if q[i] > q[j]:
                    dif += 1
            bribes += dif
        print(bribes)
def Solution2(q):
    bribes = 0
    for i in range(len(q)-1,-1,-1):
        if q[i]-(i+1)>2:
            print("Too Chaotic")
            return
        for j in range(max(0,q[i]-2),i):
            if q[j]>q[i]:
                bribes+=1
    print(bribes)



if __name__=="__main__":
    list1 = [2,1,5,3,4]
    list2 = [1,2,5,3,7,8,6,4]
    Solution3(list1)
    t1 = timeit.default_timer()
    Solution3(list2)
    t2 = timeit.default_timer()-t1
    print(t2)
    t1 = timeit.default_timer()
    Solution2(list2)
    t2 = timeit.default_timer()-t1
    print(t2)



