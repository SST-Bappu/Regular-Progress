import sys
def BellmanFordAlgo(Direction,start):
    DirectionChain = {}
    for row in Direction:
        if DirectionChain.get(row[0]):
            DirectionChain[row[0]].append([row[1], row[2]])
        else:
            DirectionChain[row[0]] = [[row[1], row[2]]]
    inf = sys.maxsize
    pathWeights = {}
    for key in DirectionChain:
        pathWeights[key] = inf
    pathWeights[start] = 0

    print(DirectionChain)
    print(pathWeights)

    while True:
        chk = False
        for key in DirectionChain:
            for row in DirectionChain[key]:
                if row[1]+pathWeights[key]<pathWeights[row[0]]:
                    pathWeights[row[0]] = row[1]+pathWeights[key]
                    chk = True
        if not chk:
            break
    max = 0
    for key in pathWeights:
        if pathWeights[key]>max:
            max = pathWeights[key]
    return max != inf

if __name__=="__main__":
    Direction = [[1,2,9],[3,2,3],[5,3,7],[3,1,5],[2,5,-3],[4,5,6],[1,4,2],[4,2,-4]]
    print(BellmanFordAlgo(Direction,1))
