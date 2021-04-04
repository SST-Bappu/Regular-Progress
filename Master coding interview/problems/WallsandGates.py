def WallsandGates(matrix):
   for i in range(len(matrix)):
       for j in range(len(matrix[0])):
           if matrix[i][j] == 0:
               FindGates(matrix,i,j)

def FindGates(matrix,row,column,count=0):
    if row<0 or row>=len(matrix) or column<0 or column>=len(matrix[0]) or matrix[row][column]<count:
        return
    matrix[row][column] = count
    FindGates(matrix,row-1,column,count+1)
    FindGates(matrix, row, column+1, count + 1)
    FindGates(matrix, row+1, column, count + 1)
    FindGates(matrix, row, column-1, count + 1)

if __name__=="__main__":
    inf = 2147483647
    matrix = [
        [inf,-1,0,inf],
        [inf,inf,inf,-1],
        [inf,-1,inf,-1],
        [0,-1,inf,inf]
    ]
    matrix1 = [
        [-1, inf,inf,inf,inf,inf, -1, -1, inf,0],
        [inf, inf,-1,inf,inf,inf,inf, inf, inf,inf],
        [-1, inf,-1,inf,inf,-1, -1, inf, -1,-1],
        [inf,inf,inf,-1,-1, -1, inf, inf, -1,inf],
        [inf,-1,-1,inf,inf, inf, inf, inf, inf,inf],
        [inf,-1,-1,inf,inf, -1, inf, -1, -1,inf],
        [inf,inf,inf,inf,-1, inf, inf, inf, inf,inf],
        [-1,inf,-1,inf,-1, inf, -1, inf, inf,inf],
        [-1,inf,-1,-1,inf, inf, inf, -1, -1,-1],
        [inf,inf,inf,inf,inf, inf, inf, -1, -1,inf]
    ]
    WallsandGates(matrix)
    for row in matrix:
        for item in row:
            print(item,end=" ")
        print(" ")
    WallsandGates(matrix1)
    print("Shortest Path is = ",matrix1[9][0])
    for row in matrix1:
        for item in row:
            print(item, end=" ")
        print(" ")
