def DFS_2DArray(matrix):
    row = len(matrix)
    column = len(matrix[0])
    seen = [[0 for i in range(column)] for j in range(row)]
    values = []
    DFS(matrix,0,0,seen,values)
    return values
def DFS(matrix,r,c,seen,values):
    if r<0 or r>=len(matrix) or c<0 or c>=len(matrix[0]) or seen[r][c]:
        return
    values.append(matrix[r][c])
    seen[r][c] = 1
    DFS(matrix,r-1,c,seen,values)
    DFS(matrix,r,c+1,seen,values)
    DFS(matrix, r+1, c, seen, values)
    DFS(matrix,r,c-1,seen,values)

if __name__=="__main__":
    list = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]
    ]
    for row in list:
        print(row)
    print(DFS_2DArray(list))

