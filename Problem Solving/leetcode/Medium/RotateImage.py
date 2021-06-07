def RotateImage(mat):
    n = len(mat)-1
    for i in range(n//2+1):
        for j in range(i,n-i):
            temp = mat[i][j]
            mat[i][j] = mat[n-j][i]
            mat[n-j][i] = mat[n-i][n-j]
            mat[n-i][n-j] = mat[j][n-i]
            mat[j][n-i] = temp

if __name__=="__main__":
    mat = [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
    RotateImage(mat)
    print(mat)

