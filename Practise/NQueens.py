import copy
def NQueens(n):
    grid = [['.' for _ in range(n)] for _ in range(n)]
    arrangements = []
    placeQueens(0,grid,arrangements)
    return arrangements
def placeQueens(r,grid,arrangements):
    if r==len(grid):
        arrangements.append(grid)
        return
    for col in range(len(grid)):
        grid[r][col] = 'Q'
        if helper(r,col,grid):
            new = copy.deepcopy(grid)
            placeQueens(r+1,new,arrangements)
        grid[r][col] = '.'
def helper(row,col,grid):
    r = row-1
    c = col-1
    while r>=0:
        if grid[r][col]=='Q':
            return False
        r-=1
    while c>=0:
        if grid[row][c]=='Q':
            return False
        c-=1
    r = row - 1
    c = col - 1
    while r>=0 and c>=0:
        if grid[r][c]=='Q':
            return False
        r-=1
        c-=1
    r = row - 1
    c = col + 1
    while r >= 0 and c < len(grid):
        if grid[r][c] == 'Q':
            return False
        r -= 1
        c += 1
    return True
if __name__=="__main__":
    result = NQueens(8)
    for item in result:
        for row in item:
            print(row)
        print("<------>")
    print(len(result))