def knightProbability(n,k,r,c):
    if k==0:
        return 1
    Direction =[[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[-1,2],[1,-2],[-1,-2]]
    return KnightMoving(Direction,n,k,r,c)
def KnightMoving(Direction,n,k,r,c):
    if r>=n or r<0 or c>=n or c<0:
        return 0
    if k==0:
        return 1
    result = 0
    for row in Direction:
        result+=KnightMoving(Direction,n,k-1,r+row[0],c+row[1])/8
    print(result)
    return result

if __name__=="__main__":
    print(knightProbability(6,2,2,2))




