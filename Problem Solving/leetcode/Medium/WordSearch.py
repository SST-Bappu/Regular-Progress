def wordSearch(grid,word):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == word[0]:
                if DFS(grid,word,i,j,0):
                    return True
    return False

def DFS(grid,word,r,c,i):
    if i == len(word):
        return True
    if r<0 or r>=len(grid) or c<0 or c>=len(grid[0]) or grid[r][c]!=word[i]:
        return False
    char = grid[r][c]
    grid[r][c] = None
    result = DFS(grid,word,r,c+1,i+1) or DFS(grid,word,r+1,c,i+1) or DFS(grid,word,r,c-1,i+1) or DFS(grid,word,r-1,c,i+1)
    grid[r][c] = char
    return result
if __name__=="__main__":
    grid = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = 'ABCCED'
    print(wordSearch(grid,word))