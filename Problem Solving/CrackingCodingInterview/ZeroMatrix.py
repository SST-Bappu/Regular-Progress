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

if __name__=="__main__":
    mat=[[1,3,5],[2,0,4],[0,5,4]]
    for row in mat:
        print(row)
    ZeroMatrix(mat)
    print("Matrix after Operation")
    for row in mat:
        print(row)