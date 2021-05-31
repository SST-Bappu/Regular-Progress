def WildCardMatch(s,p):
    dp = [[False for _ in range(len(p)+1)] for _ in range(len(s)+1)]
    dp[0][0] = True
    for i in range(len(s)+1):
        for j in range(len(p)):
            if i>0 and (p[j] == s[i-1] or p[j] == '?'):
                    dp[i][j+1] = dp[i-1][j]
            elif p[j] == '*':
                dp[i][j+1] = dp[i][j] or dp[i-1][j+1]
    return dp[-1][-1]

if __name__=="__main__":
    s = "cdb"
    p = "*c?b"
    print(WildCardMatch(s,p))