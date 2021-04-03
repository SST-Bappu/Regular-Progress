from collections import deque
def BFSthroughGraph(adjMat): #Here I used Adjacency Matrix as input
    Q = deque()
    Q.append(0)
    result=[]
    while(len(Q)):
        current = Q.popleft()
        result.append(current)
        j=0
        while j<len(adjMat[0]):
            if adjMat[current][j]==1:
                adjMat[j][current] = 0
                Q.append(j)
            j+=1
    return result


if __name__=="__main__":
    adjMat =[
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
    print(BFSthroughGraph(adjMat))

