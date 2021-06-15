def ObstacleGrid(grid):
    m = len(grid)
    n = len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                grid[i][j] = 0
                continue
            if i==0 and j==0:
                grid[i][j] = 1
            if i-1>=0:
                grid[i][j]+=grid[i-1][j]
            if j-1>=0:
                grid[i][j] += grid[i][j-1]
    return grid[m-1][n-1]
if __name__=="__main__":
    Grid = [[0,0],[0,1]]
    print(ObstacleGrid(Grid))