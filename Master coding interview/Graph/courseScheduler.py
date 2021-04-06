from collections import deque
def CourseScheduler(n, PreReq):
    ReqHash={}
    i=0
    while i<len(PreReq):
        j=1
        while j<len(PreReq[i]):
            if not ReqHash.get(PreReq[i][j]):
                ReqHash[PreReq[i][j]] = [PreReq[i][0]]
            else:
                ReqHash[PreReq[i][j]].append(PreReq[i][0])
            j+=1
        i+=1
    print(ReqHash)
    for i in range(n):
        Q = deque()
        seen = {}
        j=0
        if ReqHash.get(i):
            for item in ReqHash[i]:
                Q.append(item)
        while len(Q):
            current = Q.popleft()
            if i==current:
                return False
            seen[current]:True
            if ReqHash.get(current):
                for item in ReqHash[current]:
                    if not seen.get(current):
                        Q.append(item)
    return True
def courseScheduler_optimal(n, PreReq):
    ReqHash = {}
    InDegrees=[0 for i in range(n)]
    i = 0
    while i < len(PreReq):
        j = 1
        while j < len(PreReq[i]):
            if not ReqHash.get(PreReq[i][j]):
                ReqHash[PreReq[i][j]] = [PreReq[i][0]]
            else:
                ReqHash[PreReq[i][j]].append(PreReq[i][0])
            InDegrees[PreReq[i][0]]+=1
            j += 1
        i += 1
    print(ReqHash)
    print(InDegrees)
    i=0
    stack = []
    while i<len(InDegrees):
        if InDegrees[i]==0:
            stack.append(i)
        i+=1
    count = 0
    print(stack)
    while len(stack):
        count+=1
        current = stack.pop()
        j=0
        adjacent = ReqHash[current]
        while j < len(adjacent):
            item = adjacent[j]
            InDegrees[item]-=1
            if InDegrees[item]==0:
                stack.append(item)
            j+=1
    print(count)
    print(InDegrees)
    return count == n



if __name__=="__main__":
    PreReq = [[1,0],[2,1],[2,5],[0,3],[4,3],[3,5],[4,5]]
    print(CourseScheduler(6,PreReq))
    print(courseScheduler_optimal(6,PreReq))