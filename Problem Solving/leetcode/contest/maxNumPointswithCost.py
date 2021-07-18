def maxPoints(matrix):
    TotalPoints = 0
    lastCol = 0
    for i in range(len(matrix)):
        cur = 0
        for j in range(len(matrix[0])):
            if i==0:
                if matrix[i][j]>cur:
                    cur = matrix[i][j]
                    lastCol = j
            else:
                point = matrix[i][j]-abs(lastCol-j)
                if point>cur:
                    cur = point
                    lastCol = j
        TotalPoints+=cur
    return TotalPoints

if __name__=="__main__":
    matrix = [[1,5],[2,3],[4,2]]
    print(maxPoints(matrix))
