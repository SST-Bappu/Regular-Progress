def SpiralMove(n):
    k= 0
    result = [[False for _ in range(n)] for _ in range(n)]
    total = 1
    while total<=n*n:
        i = k
        j = k
        chk = False
        while j<n-k-1:
            result[i][j] = total
            total+=1
            chk = True
            j+=1
        while i<n-k:
            result[i][j] = total
            total += 1
            i+=1
        if chk:
            j-=1
        if i>k:
            i-=1
        while j>k and i>k:
            result[i][j] = total
            total += 1
            j-=1

        while chk and i>k:
            result[i][j] = total
            total += 1
            i-=1
        k+=1
    return result
if __name__=="__main__":
    result = SpiralMove(5)
    for row in result:
        print(row)