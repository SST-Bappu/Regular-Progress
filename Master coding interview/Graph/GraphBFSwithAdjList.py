from collections import deque
def BFSthroughGraph_AdjList(adjList): #Here I used Adjacency List as input
    result =[]
    Q = deque()
    Q.append(0)
    while len(Q):
        current = Q.popleft()
        result.append(current)
        for item in adjList[current]:
            Q.append(item)
            adjList[item].remove(current)
    return result

if __name__=="__main__":
    adjList = {
        0: [1, 3],
        1: [0],
        2: [3, 8],
        3: [0, 2, 4, 5],
        4: [3, 6],
        5: [3],
        6: [4, 7],
        7: [6],
        8: [2]
    }
    print(BFSthroughGraph_AdjList(adjList))