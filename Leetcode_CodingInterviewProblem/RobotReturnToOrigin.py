def RobotMove(grid,moves):
    x = grid[0][0]
    y = grid[0][1]
    for c in moves:
        if c == 'U' or ord(c)-ord('U')==32:
            y+=1
        elif c=='D' or ord(c)-ord('D')==32:
            y-=1
        elif c=='L' or ord(c)-ord('L')==32:
            x-=1
        elif c=='R' or ord(c)-ord('R') == 32:
            x+=1
    return [x,y]
if __name__=="__main__":
    grid = [[0,0]]
    print(RobotMove(grid,"uDRl"))
