def PaintFill(screen,r,c,color):
    current = screen[r][c]
    if current==color:
        return False
    return floodFill(screen,r,c,color,current)
def floodFill(screen, r,c,color,current):
    if r<0 or r>=len(screen) or c<0 or c>=len(screen[0]) or screen[r][c]!=current:
        return False
    screen[r][c] = color
    floodFill(screen,r-1,c,color,current)
    floodFill(screen,r+1,c,color,current)
    floodFill(screen,r,c+1,color,current)
    floodFill(screen,r,c-1,color,current)
    return True
if __name__=="__main__":
    screen =[[1,1,1,1,1,1],[1,1,2,2,1,1],[1,1,2,2,1,1],[2,2,2,2,2,2]]
    print(PaintFill(screen,2,0,5))
    for row in screen:
        print(row)

