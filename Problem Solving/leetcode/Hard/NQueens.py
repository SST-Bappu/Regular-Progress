from copy import deepcopy
class PlaceNQueens:
    def NQueens(self,n):
        board =[['.' for _ in range(n)]for _ in range(n)]
        self.arrangement = []
        self.PlaceQ(board,0,n)
        final = []
        for sol in self.arrangement:
            newSol = []
            for row in sol:
                newSol.append(''.join(row))
            final.append(newSol)
        return final
    def PlaceQ(self,board,r,n):
        if r == n:
            self.arrangement.append(board)
            return
        for i in range(n):
            if self.checkPlace(board,n,r-1,i):
                board[r][i] = 'Q'
                new = deepcopy(board)
                self.PlaceQ(new,r+1,n)
                board[r][i] = '.'


    def checkPlace(self,board,n,r,c):
        i = r
        j = c-1
        k = c+1
        while i >= 0:
            if board[i][c] == 'Q':
                return False
            if j >= 0 and board[i][j] == 'Q':
                return False
            if k < n and board[i][k] == 'Q':
                return False
            i -= 1
            j -= 1
            k += 1
        return True

if __name__=="__main__":
    sol = PlaceNQueens()
    result = sol.NQueens(4)
    print(len(result))
    for sol in result:
        print("-----><-----><------><------")
        for row in sol:
            print(row)