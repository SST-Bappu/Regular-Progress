def MinPathSum(grid):
    m = len(grid)
    n = len(grid[0])
    for i in range(m):
        for j in range(n):
            if i - 1 >= 0 and j-1>=0:
                grid[i][j] += min(grid[i - 1][j],grid[i][j-1])
            elif j - 1 >= 0:
                grid[i][j] += grid[i][j - 1]
            elif i-1>=0:
                grid[i][j] += grid[i-1][j]
    return grid[m - 1][n - 1]

if __name__=="__main__":
    grid = [[1,2,3],[4,5,6]]
    print(MinPathSum(grid))