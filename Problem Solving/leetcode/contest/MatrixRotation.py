def Rotation(mat1,target):
    n = len(mat1)-1
    k=0
    while k<4:
        for i in range(n//2+1):
            dest = n-i
            for j in range(i,dest):
                temp1 = mat1[i][j]
                mat1[i][j] = mat1[n-j][i]
                mat1[n-j][i] = mat1[n-i][n-j]
                mat1[n-i][n-j] = mat1[j][n-i]
                mat1[j][n-i] = temp1
        if mat1==target:
            return True
        print(mat1)
        k+=1
    return False
if __name__=="__main__":
    mat1 = [[0,1,0,1,0,1],[0,1,0,1,1,0],[1,1,1,0,1,0],[0,0,0,1,0,0],[1,1,0,1,0,1],[1,1,1,0,0,1]]
    mat2 = [[1,0,0,0,1,1],[0,1,1,0,0,0],[1,1,0,1,1,0],[0,0,1,0,0,1],[1,1,1,0,1,1],[0,0,1,0,1,1]]
    # mat1 = [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
    # mat2 = [[0,1],[1,0]]
    print(Rotation(mat1,mat2))
