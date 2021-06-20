def countSubIslands(grid1,matrix):
    count = 0
    i = 0
    islands = []
    seen = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
    while (i < len(matrix)):
        j = 0
        while j < len(matrix[0]):
            if matrix[i][j] == 1 and not (seen[i][j]):
                cells = [[i,j]]
                seen[i][j] = 1
                Traverse(matrix, cells, seen, i - 1, j)
                Traverse(matrix, cells, seen, i, j + 1)
                Traverse(matrix, cells, seen, i + 1, j)
                Traverse(matrix, cells, seen, i, j - 1)
                islands.append(cells)
            j += 1
        i += 1
    for cell in islands:
        chk = True
        for index in cell:
            if grid1[index[0]][index[1]]==0:
                chk = False
                break
        if chk:
            count+=1

    return count



def Traverse(matrix, cells, seen, i, j):
    if i >= len(matrix) or i < 0 or j >= len(matrix[0]) or j < 0 or matrix[i][j] == 0 or seen[i][j]:
        return
    seen[i][j] = 1
    cells.append([i,j])
    Traverse(matrix, cells, seen, i - 1, j)
    Traverse(matrix, cells, seen, i, j + 1)
    Traverse(matrix, cells, seen, i + 1, j)
    Traverse(matrix, cells, seen, i, j - 1)
if __name__=="__main__":
    matrix = [
            [1,1,0,1,0],
            [1,0,1,0,1],
            [0,1,1,1,0],
            [1,0,1,0,1]
        ]
    count, result = countSubIslands(matrix)
    print(count)
    for cell in result:
        print(cell)