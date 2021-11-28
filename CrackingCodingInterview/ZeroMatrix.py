def ZeroMatrix(mat):
    keep=[]
    for i in range(len(mat)):
        if i in keep:
            continue
        for j in range(len(mat)):
            if i in keep:
                break
            if j in keep:
                continue
            if mat[i][j]==0:
                for k in range(len(mat)):
                    mat[i][k]=0
                    mat[k][j]=0
                keep.append(i)
                if i!=j:
                    keep.append(j)
def zeroMatrix_optimized(matrix):
    col = [False for _ in range(len(matrix[0]))]
    row =[False for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]==0:
                row[i] = True
                col[j] = True
    for i in range(len(row)):
        if row[i]:
            nullifyRow(matrix,i)

    for i in range(len(col)):
        if col[i]:
            nullifyCol(matrix,i)
def nullifyRow(matrix,row):
    for i in range(len(matrix)):
        matrix[row][i] = 0
def nullifyCol(matrix,col):
    for i in range(len(matrix[0])):
        matrix[i][col] = 0

if __name__=="__main__":
    mat=[[1,3,5],[2,0,4],[0,5,4]]
    for row in mat:
        print(row)
    # # ZeroMatrix(mat)
    # print("Matrix after Operation")
    # for row in mat:
    #     print(row)
    print("Optimized:")
    zeroMatrix_optimized(mat)
    for row in mat:
        print(row)
