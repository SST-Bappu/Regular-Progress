#TopDown approach using Dynamic Programming
def RobotOnGrid(maze):
   if not maze:
       return None
   path =[]
   failedPoints = set()
   getPath(maze,len(maze)-1,len(maze[0])-1,path,failedPoints)
   return path
def getPath(maze,row,col,path,failedPoints):
    if row<0 or col<0 or not maze[row][col]:
        return False
    point = (row,col)
    if point in failedPoints:
        return False
    is_at_origin = row==0 and col==0
    if is_at_origin or getPath(maze,row,col-1,path,failedPoints) or getPath(maze,row-1,col,path,failedPoints):
        path.append(point)
        return True
    failedPoints.add(point)
    return False
def RobotOnGrid_BottomUp(maze):
    if not maze:
        return
    path =[]
    failedPoint = set()
    FindPaths(maze,0,0,path,failedPoint)
    return path
def FindPaths(maze,row,col,path,failedPoints):
    if row>=len(maze) or col>=len(maze[0]) or not maze[row][col]:
        return False
    point = (row,col)
    if point in failedPoints:
        return False
    is_at_origin = row == len(maze)-1 and col == len(maze[0])-1
    if is_at_origin or FindPaths(maze,row+1,col,path,failedPoints) or FindPaths(maze,row,col+1,path,failedPoints):
        path.append(point)
        return True
    failedPoints.add(point)
    return False
if __name__=="__main__":
    print(RobotOnGrid([[True,True],[False,True]]))
    print(RobotOnGrid_BottomUp([[True,True],[False,True]]))