def suduku(board):
    rows = [dict() for _ in range(len(board))]
    cols = [dict() for _ in range(len(board))]
    boxId = [dict() for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]!=0:
                val = board[i][j]
                rows[i][val] = True
                cols[j][val] = True
                box = getBoxId(i,j)
                boxId[box][val] = True
    return solver(rows,cols,boxId,board,0,0)

def solver(rows,cols,boxId,board,r,c):
    if r==len(board) or c==len(board[0]):
        return True
    if board[r][c]==0:
        box = getBoxId(r,c)
        for i in range(1,10):
            if is_valid(rows,cols,boxId,box,r,c,i):
                board[r][c] = i
                rows[r][i] = True
                cols[c][i] = True
                boxId[box][i] = True
                if c==len(board[0])-1:
                    if solver(rows,cols,boxId,board,r+1,0):
                        return True
                else:
                    if solver(rows,cols,boxId,board,r,c+1):
                        return True
                del rows[r][i]
                del cols[c][i]
                del boxId[box][i]
            board[r][c]=0
    else:
        if c == len(board[0])- 1:
            solver(rows, cols, boxId, board, r + 1, 0)
        else:
            solver(rows, cols, boxId, board, r, c + 1)
def getBoxId(row,col):
    cur_row = row//3
    cur_col = (col//3)*2
    return cur_col+cur_row
def is_valid(rows,cols,boxId,box,r,c,val):
    if rows[r].get(val) or cols[c].get(val) or boxId[box].get(val):
        return False
    return True

if __name__=="__main__":
    grid = [
        [3, 0, 6, 5, 0, 8, 4, 0, 0],
         [5, 2, 0, 0, 0, 0, 0, 0, 0],
         [0, 8, 7, 0, 0, 0, 0, 3, 1],
         [0, 0, 3, 0, 1, 0, 0, 8, 0],
         [9, 0, 0, 8, 6, 3, 0, 0, 5],
         [0, 5, 0, 0, 9, 0, 6, 0, 0],
         [1, 3, 0, 0, 0, 0, 2, 5, 0],
         [0, 0, 0, 0, 0, 0, 0, 7, 4],
         [0, 0, 5, 2, 0, 6, 3, 0, 0]
    ]
    print(suduku(grid))
    for row in grid:
        print(row)

