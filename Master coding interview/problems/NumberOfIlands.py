def NumberOfIlands(matrix):
    count = 0
    i = 0
    seen =[[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
    while(i<len(matrix)):
        j=0
        while j<len(matrix[0]):
            if matrix[i][j]==1 and not(seen[i][j]):
                seen[i][j] = 1
                Traverse(matrix,seen,i-1,j)
                Traverse(matrix,seen,i,j+1)
                Traverse(matrix,seen,i+1,j)
                Traverse(matrix,seen,i,j-1)
                count+=1
            j+=1
        i+=1
    return count
def Traverse(matrix,seen,i,j):
    if i>=len(matrix) or i<0 or j>=len(matrix[0]) or j<0 or matrix[i][j]==0 or seen[i][j]:
        return
    seen[i][j]=1
    Traverse(matrix, seen, i - 1, j)
    Traverse(matrix, seen, i, j + 1)
    Traverse(matrix, seen, i + 1, j)
    Traverse(matrix, seen, i, j - 1)

if __name__=="__main__":
    matrix = [
        [1,1,0,1,0],
        [1,0,1,0,1],
        [0,1,1,1,0],
        [1,0,1,0,1]
    ]
    print(NumberOfIlands(matrix))