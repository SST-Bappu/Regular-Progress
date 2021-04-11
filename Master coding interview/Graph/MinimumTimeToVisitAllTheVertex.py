def Dijkastra_ShortestPath(Direction, start):
    DirectionChain = {}
    for row in Direction:
        if DirectionChain.get(row[0]):
            DirectionChain[row[0]].append([row[1],row[2]])
        else:
            DirectionChain[row[0]]=[[row[1],row[2]]]
    inf = 140014
    pathWeights = {}
    for key in DirectionChain:
        pathWeights[key] = inf
    pathWeights[start] = 0
    track = [start]
    seen= [None for i in range(len(DirectionChain))]
    while len(track):
        current = 0
        i=1
        while i< len(track):
            if pathWeights[track[i]]<pathWeights[track[current]]:
                current = i
            i+=1
        current = track.pop(current)
        for row in DirectionChain[current]:
            if (row[1] + pathWeights[current]) < pathWeights[row[0]]:
                pathWeights[row[0]] = row[1] + pathWeights[current]
            if not seen[current-1] and DirectionChain.get(row[0]):
                track.append(row[0])
        seen[current-1] = 1
    return pathWeights
def MinimumTime(Direction, start):
    ShortestTime=Dijkastra_ShortestPath(Direction,start)
    maxTime = 0
    for key in ShortestTime:
       maxTime = max(maxTime,ShortestTime[key])

    return maxTime

if __name__=="__main__":
    Direction = [[1,2,9],[1,4,2],[2,5,1],[4,2,4],[4,5,6],[5,3,7],[3,1,5]]
    print(MinimumTime(Direction,1))
