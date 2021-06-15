def UniquePaths(m,n):
    grid = [[0 for _ in range(n)]for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if i==0 and j==0:
                grid[i][j]=1
                continue
            if i-1>=0:
                grid[i][j]+=grid[i-1][j]
            if j-1>=0:
                grid[i][j]+=grid[i][j-1]
    return grid[m-1][n-1]

if __name__=="__main__":
    print(UniquePaths(3,3))