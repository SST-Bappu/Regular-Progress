class Sudoku:
    def SudokuSolver(self,grid):
        self.row = [dict() for _ in range(len(grid))]
        self.col = [dict() for _ in range(len(grid[0]))]
        self.seg = [dict() for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]!='.':
                    self.row[i][grid[i][j]] = True
                    self.col[j][grid[i][j]] = True
                    segmentId = self.generateSegmentId(i, j)
                    self.seg[segmentId][grid[i][j]] = True
        self.fillEmptyCell(grid,0,0)
    def fillEmptyCell(self,grid,r,c):
        if r==len(grid):
            return True
        if grid[r][c]!='.':
            if c== len(grid[0])-1:
                return self.fillEmptyCell(grid,r+1,0)
            else:
                return self.fillEmptyCell(grid,r,c+1)
        else:
            segmentId = self.generateSegmentId(r, c)
            for i in range(1,10):
                val = str(i)
                if self.is_valid(val,r,c,segmentId):
                    self.row[r][val] = True
                    self.col[c][val] = True
                    self.seg[segmentId][val] = True
                    grid[r][c] = val
                    if c==len(grid)-1:
                        if self.fillEmptyCell(grid,r+1,0):
                            return True
                    else:
                        if self.fillEmptyCell(grid,r,c+1):
                            return True
                    del self.row[r][val]
                    del self.col[c][val]
                    del self.seg[segmentId][val]
            grid[r][c] = "."
            return False



    def is_valid(self,i,r,c,segmentId):
        if self.row[r].get(i) or self.col[c].get(i) or self.seg[segmentId].get(i):
            return False
        return True

    def generateSegmentId(self,row,col):
        cur_row = row//3
        cur_col = (col//3)*3
        return cur_row+cur_col

if __name__=="__main__":
    grid = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    sol = Sudoku()
    sol.SudokuSolver(grid)
    for row in grid:
        print(row)