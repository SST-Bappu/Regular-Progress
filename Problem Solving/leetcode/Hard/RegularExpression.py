def RegularExpression(s,p):
    countStar= 0
    for i in p:
        if i=='*':
            countStar+=1
    m = len(s)
    t = len(p)
    n = t-countStar
    dp = [[False for _ in range(n+1)]for _ in range(m+1)]
    dp[0][0] = True
    for i in range(m+1):
        k = 0
        for j in range(n):
            if i==0:
                if k+1<t and p[k+1] == '*':
                    dp[i][j + 1] = dp[i][j]
                    k+=1
            else:
                if (p[k]=='.' or s[i-1] == p[k]) and (k+1<t and p[k+1]=='*'):
                        dp[i][j+1] = dp[i-1][j+1] or dp[i-1][j]
                        k+=1
                elif p[k] == '.' or s[i-1] == p[k]:
                    dp[i][j+1] = dp[i-1][j]
                elif k+1<t and p[k+1]=='*':
                    dp[i][j+1] = dp[i][j]
                    k+=1
            k+=1
    for row in dp:
        print(row)
    return dp[-1][-1]
if __name__=="__main__":
    s = "aasdfasdfasdfasdfas"
    p ="aasdf.*asdf.*asdf.*asdf.*s"
    print(RegularExpression(s,p))

