from collections import deque
def BFSthroughGraph(adjList):
    Q = deque()
    seen = [None for i in range(len(adjList[0]))]
    Q.append(0)
    result=[]
    while(len(Q)):
        n = len(Q)
        count = 0
        while count<n:
            current = Q.popleft()
            result.append(current)
            seen[current] = 1
            j=0
            while j<len(adjList[0]):
                if adjList[current][j]==1 and not seen[j]:
                    Q.append(j)
                j+=1
            count+=1
    return result
if __name__=="__main__":
    adjList =[
        [0,1,0,1,0,0,0,0,0],
        [1,0,0,0,0,0,0,0,0],
        [0,0,0,1,0,0,0,0,1],
        [1,0,1,0,1,1,0,0,0],
        [0,0,0,1,0,0,1,0,0],
        [0,0,0,1,0,0,0,0,0],
        [0,0,0,0,1,0,0,1,0],
        [0,0,0,0,0,0,1,0,0],
        [0,0,1,0,0,0,0,0,0],
    ]
    print(BFSthroughGraph(adjList))
