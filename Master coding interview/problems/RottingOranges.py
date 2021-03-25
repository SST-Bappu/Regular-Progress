def RottingOranges(matrix):
    minutes = -1
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]==2:
                Q = [[i,j]]
                matrix[i][j] = 1
                while len(Q):
                    l= len(Q)
                    count=0
                    minutes+=1
                    while count<l:
                        current = Q.pop(0)
                        r = current[0]
                        c = current[1]
                        if (r>=0 and r<len(matrix) and c>=0 and c<len(matrix[0]) and matrix[r][c]==1):
                            print(matrix[r][c],end=" ")
                            matrix[r][c]=0
                            Q.append([r-1,c])
                            Q.append([r, c+1])
                            Q.append([r+1, c])
                            Q.append([r, c-1])
                        count+=1
    print("")
    return minutes

if __name__=="__main__":
    matrix = [
        [2,1,1,0,0],
        [1,1,1,0,0],
        [0,1,1,1,1],
        [0,1,0,0,1]
    ]

    print(RottingOranges(matrix))