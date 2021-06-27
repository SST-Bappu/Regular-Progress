def CyclicalRot(mat,L):
    m = len(mat)
    n = len(mat[0])
    t = min(m,n)
    p = (t//2)*max(m,n)+t
    # L = L%p
    while L:
        for i in range(t//2):
            j = m-1-i
            k = n-1-i
            last = last = mat[j][k]
            while j>i:
                temp = mat[j-1][k]
                mat[j-1][k] = last
                last = temp
                j-=1
            while k>i:
                temp = mat[j][k-1]
                mat[j][k-1] = last
                last = temp
                k-=1
            while j<(m-1-i):
                temp = mat[j+1][k]
                mat[j+1][k] = last
                last = temp
                j+=1
            while k<(n-i-1):
                temp = mat[j][k+1]
                mat[j][k+1] = last
                last = temp
                k+=1
        L-=1
if __name__=="__main__":
    mat = [[10,1,4,8],[6,6,3,10],[7,4,7,10],[1,10,6,1],[2,1,1,10],[3,8,9,2],[7,1,10,10],[7,1,4,9],[2,2,4,2],[10,7,5,10]]
    #mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    CyclicalRot(mat,24)
    for row in mat:
        print(row)
