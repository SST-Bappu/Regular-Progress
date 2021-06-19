def SetMatrix(matrix):
    Iindex = set()
    Jindex = set()
    m = len(matrix)
    n = len(matrix[0])
    stack = []
    for i in range(m):
        if i in Iindex:
            continue
        for j in range(n):
            if i in Iindex or j in Jindex:
                continue
            if matrix[i][j] == 0:
                stack.append([i,j])
            while stack:
                cur = stack.pop()
                if cur[0] not in Iindex:
                    Iindex.add(cur[0])
                    for k in range(n):
                        if (k in Jindex) or (k==cur[1]):
                            continue
                        if matrix[cur[0]][k] == 0:
                            stack.append([cur[0],k])
                        matrix[cur[0]][k] = 0
                if cur[1] not in Jindex:
                    Jindex.add(cur[1])
                    for l in range(m):
                        if (l in Iindex) or (l == cur[0]):
                            continue
                        if matrix[l][cur[1]] == 0:
                            stack.append([l,cur[1]])
                        matrix[l][cur[1]] = 0
if __name__=="__main__":
    matrix = [[0,1,2,0],[3,4,5,2],[4,3,1,5]]
    SetMatrix(matrix)
    for row in matrix:
        print(row)

