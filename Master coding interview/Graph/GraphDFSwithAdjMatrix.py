def GraphDFSwithAdjMatrix(adjMat):
    result = []
    DFS(0,adjMat,result)
    return result
def DFS(Node,adjMat,result):
    result.append(Node)
    i=0
    while i <len(adjMat[0]):
        if adjMat[Node][i]==1:
            adjMat[i][Node] = 0
            DFS(i,adjMat,result)
        i+=1
if __name__=="__main__":
    adjMat = [
        [0, 1, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
    ]
    print(GraphDFSwithAdjMatrix(adjMat))