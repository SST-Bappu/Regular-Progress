def isInterleaving(s1,s2,s3):
    m = len(s1)
    n = len(s2)
    if m+n!=len(s3):
        return False
    memo = [[False for _ in range(m+1)]for _ in range(n+1)]
    memo[0][0] = True
    for i in range(n+1):
        if i>0:
            if s2[i-1]==s3[i-1]:
                memo[i][0] = memo[i-1][0]
        for j in range(1,m+1):
            if i==0:
                if s1[j-1]==s3[j-1]:
                    memo[i][j] = memo[i][j-1]
            else:
                t1 = t2 = False
                if s1[j-1] == s3[i+j-1]:
                    t1 = True
                if s2[i-1] == s3[i+j-1]:
                    t2 = True

                if t1 and t2:
                    memo[i][j] = memo[i][j-1] or memo[i-1][j]
                elif t1:
                    memo[i][j] = memo[i][j-1]
                elif t2:
                    memo[i][j] = memo[i-1][j]
                else:
                    memo[i][j] = False
    return memo[n][m]

if __name__=="__main__":
    s1 = "db"
    s2 = "b"
    s3 = "cbb"
    print(isInterleaving(s1,s2,s3))