def ShortestPath(Direction, start, end):
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
    pathWeights[end] = inf
    pathWeights[start] = 0
    track = [start]
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
            if DirectionChain.get(row[0]):
                track.append(row[0])
    return pathWeights[end]



if __name__=="__main__":
    Direction = [[0,1,4],[0,2,2],[1,3,1],[2,4,5],[2,3,6],[3,5,4],[4,5,10]]
    print(ShortestPath(Direction,0,5))