import copy
def queens(n):
    arrangements=[]
    board = [['.' for _ in range(n)] for _ in range(n)]
    helper(0,board,arrangements)
    return arrangements
def helper(row,board,arrangements):
    if row==len(board):
        arrangements.append(board)
        return
    for col in range(len(board[row])):
        if is_valid(row,col,board):
            board[row][col] = 'Q'
            helper(row+1,copy.deepcopy(board),arrangements)
            board[row][col]='.'
def is_valid(row,col,board):
    for cur_row in range(len(board)):
        if cur_row!=row and board[cur_row][col]=='Q':
            return False
    for cur_col in range(len(board[row])):
        if cur_col!=col and board[row][cur_col]=='Q':
            return False
    cur_col= col-1
    cur_row= row-1
    while cur_row>=0 and cur_col>=0:
        if board[cur_row][cur_col]=='Q':
            return False
        cur_col-=1
        cur_row-=1
    cur_col = col + 1
    cur_row = row - 1
    while cur_row>=0 and cur_col<len(board):
        if board[cur_row][cur_col]=='Q':
            return False
        cur_col+=1
        cur_row-=1
    return True
if __name__=="__main__":
    result = queens(8)
    for board in result:
        for row in board:
            print(row)
        print("-->>><<<--")
    print(len(result))
