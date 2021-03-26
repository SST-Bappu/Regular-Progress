def WallsandGates(matrix):
    if len(matrix)<=0:
        return
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 21474:
                matrix[i][j] = -1
                seen = [[False for k in range(len(matrix[0]))]for l in range(len(matrix))]
                matrix[i][j]=FindGates(matrix,i,j,seen)

def FindGates(matrix,row,column,seen,count=0):
    if (row<0 or row>=len(matrix) or column<0 or column>=len(matrix[0]) or matrix[row][column]==-1 or seen[row][column]):
        return 21475
    if matrix[row][column]==0:
        return count
    seen[row][column] = True
    return min(FindGates(matrix,row-1,column,count+1),FindGates(matrix,row,column+1,count+1),
               FindGates(matrix,row+1,column,count+1),FindGates(matrix,row,column-1,count+1))
if __name__=="__main__":
    matrix=[
        [21474,-1,0,21474],
        [21474,21474,21474,-1],
        [21474,-1,21474,-1],
        [0,-1,21474,21474]
    ]
    WallsandGates(matrix)
    for row in matrix:
        for item in row:
            print(item, end=" ")
        print(" ")