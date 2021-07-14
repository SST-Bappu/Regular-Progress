def MaximalRectangle(matrix):
    n = len(matrix)
    m = len(matrix[0])
    histograms = [[0 for _ in range(m)]for _ in range(n+1)]
    i = 0
    for row in matrix:
        j = 0
        while j<m:
            if row[j]=='1':
                histograms[i+1][j] = histograms[i][j]+1
            j+=1
        i+=1
    maxArea = 0
    for row in histograms:
        n = len(row)
        left = [0 for _ in range(n)]
        left[0] = -1
        i = 1
        while i<n:
            point = i-1
            while point>=0 and row[point]>=row[i]:
                point = left[point]
            left[i] = point
            i+=1
        right = [0 for _ in range(n)]
        right[-1] = n
        i = n-2
        while i>=0:
            point = i+1
            while point<n and row[point]>= row[i]:
                point = right[point]
            right[i] = point
            i-=1
        for i in range(n):
            sol = (right[i]-left[i]-1)*row[i]
            maxArea = max(maxArea,sol)
    return maxArea

if __name__=="__main__":
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    print(MaximalRectangle(matrix))