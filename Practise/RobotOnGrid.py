def RobotGrid(grid):
    path = []
    RobotMove(grid,len(grid)-1,len(grid[0])-1,path)
    return path
def RobotMove(grid,r,c,path,failedPoint=set()):
    if r<0 or c<0 or not grid[r][c]:
        return 0
    if (r,c) in failedPoint:
        return 0
    if (r==0 and c==0) or RobotMove(grid,r-1,c,path,failedPoint) or RobotMove(grid,r,c-1,path,failedPoint):
        path.append([r,c])
        return 1
    failedPoint.add([r,c])
    return 0
if __name__=="__main__":
    grid = [
        [1,1,0,1],
        [0,1,1,1],
        [1,0,1,0],
        [1,1,1,1]
    ]
    print(RobotGrid(grid))
