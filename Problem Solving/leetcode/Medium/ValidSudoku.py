def ValidSudoku(grid):
    row = [dict() for _ in range(len(grid))]
    col = [dict() for _ in range(len(grid[0]))]
    seg = [dict() for _ in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]!='.':
                if row[i].get(grid[i][j]):
                    return False
                else:
                    row[i][grid[i][j]] = i+1
                if col[j].get(grid[i][j]):
                    return False
                else:
                    col[j][grid[i][j]] = j+1
                segmentId = generateSegmentId(i,j)
                if seg[segmentId].get(grid[i][j]):
                    return False
                else:
                    seg[segmentId][grid[i][j]] = segmentId+1
    return True

def generateSegmentId(row,col):
    cur_row = row//3
    cur_col = (col//3)*3
    return cur_row+cur_col

if __name__=="__main__":
    grid = [
        ["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]
    ]
    print(ValidSudoku(grid))