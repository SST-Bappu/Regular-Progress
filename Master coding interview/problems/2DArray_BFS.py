def BFS_2DArray(matrix):
    column = len(matrix[0])
    row = len(matrix)
    seen = [[0 for i in range(column)]for j in range(row)]
    values=[]
    Q = [[0,0]]
    count = 0
    while(count<len(Q)):
        current = Q[count]
        r = current[0]
        c = current[1]
        if not (r < 0 or r >= len(matrix) or c < 0 or c >= len(matrix[0]) or seen[r][c]):
            values.append(matrix[r][c])
            Q.append([r-1,c])
            Q.append([r, c + 1])
            Q.append([r + 1, c])
            Q.append([r, c + 1])
            seen[r][c] = 1
        count+=1
    return values
if __name__=="__main__":
    list = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    for row in list:
        print(row)
    print(BFS_2DArray(list))
