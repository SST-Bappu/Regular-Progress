def GraphDFSwithAdjList(adjList):
    result = []
    DFS(0,adjList,result)
    return result
def DFS(Node,adjList,result):
    result.append(Node)
    for item in adjList[Node]:
        adjList[item].remove(Node)
        DFS(item,adjList,result)


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
    print(GraphDFSwithAdjList(adjList))