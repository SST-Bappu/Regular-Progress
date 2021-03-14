def RotateMatrix(mat):
    m = len(mat)
    n = m-1
    if len(mat)==0 or len(mat)!=len(mat[0]):
        return False
    for i in range(m//2):
        k = n-i
        for j in range(i,k):
            temp1 = mat[i][j]
            mat[i][j] = mat[n-j][i]
            mat[n-j][i]=mat[n-i][n-j]
            mat[n-i][n-j] = mat[j][n-i]
            mat[j][n-i]=temp1
    return True
if __name__=="__main__":
    mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    print(RotateMatrix(mat))
    for row in mat:
        print(row)
