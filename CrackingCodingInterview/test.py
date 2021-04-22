def test():
    board = [
        [2,4,6,8,9],
        [8,7,10,12,5],
        [20,24,78,69,5],
        [45,44,32,15,10],
        [47,78,98,63,20]
    ]
    rows = [dict() for _ in range(len(board))]
    cols = [dict() for _ in range(len(board))]
    boxId = [dict() for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != '.':
                val = board[i][j]
                rows[i][val] = True
                cols[j][val] = True
                box = getBoxId(i, j)
                boxId[box][val] = True
    print(rows)
    print(cols)
    print(boxId)
def getBoxId(row,col):
    cur_row = row//3
    cur_col = (col//3)*2
    return cur_col+cur_row

if __name__=="__main__":
    test()