from collections import deque
def TimeNeeded(n,headId,managers,inFormTime): #It's solved using BFS
    AdjList = dict()
    i=0
    while i<n:
        if AdjList.get(managers[i]):
            AdjList[managers[i]].append(i)
        else:
            AdjList[managers[i]] = [i]
        i+=1
    Q = deque()
    Q.append(headId)
    time = 0
    curTime = 0
    while len(Q):
        n = len(Q)
        count=0
        time+=curTime
        curTime = 0
        while count<n:
            current = Q.popleft()
            if AdjList.get(current):
                curTime = max(curTime, inFormTime[current])
                for item in AdjList[current]:
                    Q.append(item)
            count+=1
    return time
def TimeNeeded_DFS(n,headId,managers,inFormTime): #Here the same problem is solved using BFS
    AdjList = dict()
    i = 0
    while i < n:
        if AdjList.get(managers[i]):
            AdjList[managers[i]].append(i)
        else:
            AdjList[managers[i]] = [i]
        i += 1
    return DFS(AdjList,headId,inFormTime)
def DFS(AdjList, Node, inFormTime):
    if not AdjList.get(Node):
        return 0
    time = 0
    i=0
    while i<len(AdjList[Node]):
        curTime = DFS(AdjList,AdjList[Node][i],inFormTime)
        time = max(time,curTime)
        i+=1
    return inFormTime[Node]+time

if __name__=="__main__":
    managers = [2,2,4,6,-1,4,4,5]
    inFromTime=[0,0,8,0,7,3,6,0]
    print(TimeNeeded(8,4,managers,inFromTime))
    print(TimeNeeded_DFS(8,4,managers,inFromTime))
