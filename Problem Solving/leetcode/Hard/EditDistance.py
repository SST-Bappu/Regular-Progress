def EditDistance(word1,word2):
    m = len(word1)+1
    n = len(word2)+1
    dp = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if i==0:
                dp[i][j] = j
            elif j==0:
                dp[i][j] = i
            else:
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])
    for row in dp:
        print(row)
    return dp[m-1][n-1]
if __name__=="__main__":
    word1 = 'sea'
    word2 = 'ate'
    print(EditDistance(word1,word2))