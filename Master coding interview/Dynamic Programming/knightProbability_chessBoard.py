def knightProbability(n,k,r,c):
    if k==0:
        return 1
    Direction =[[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[-1,2],[1,-2],[-1,-2]]
    dp =[[[-1 for i in range(n)] for j in range(n)] for l in range(k+1)]
    return KnightMoving(Direction,dp,n,k,r,c)
#Top Down Approach using Dynamic Programming
def KnightMoving(Direction,dp,n,k,r,c):
    if r>=n or r<0 or c>=n or c<0:
        return 0
    if k==0:
        return 1
    if dp[k][r][c]!=-1:
        return dp[k][r][c]
    dp[k][r][c] = 0
    for row in Direction:
        dp[k][r][c]+=KnightMoving(Direction,dp,n,k-1,r+row[0],c+row[1])/8
    return dp[k][r][c]

#Bottom up approach
def KnightProbability_BottomUP(n,k,r,c):
    Direction = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [-1, 2], [1, -2], [-1, -2]]
    dp = [[[0 for i in range(n)] for j in range(n)] for l in range(k + 1)]
    dp[0][r][c] = 1
    l=1
    while l<=k:
        i=0
        while i<n:
            j=0
            while j<n:
                for row in Direction:
                    if (i+row[0])<n and (i+row[0])>=0 and (j+row[1])<n and (j+row[1]>=0):
                        dp[l][i][j] += dp[l-1][i+row[0]][j+row[1]]/8
                j+=1
            i+=1
        l+=1
    result = 0

    for row in dp[k]:
        for item in row:
            result+=item
    return result


if __name__=="__main__":
    print(knightProbability(6,2,2,2))
    print(KnightProbability_BottomUP(6,2,2,2))





