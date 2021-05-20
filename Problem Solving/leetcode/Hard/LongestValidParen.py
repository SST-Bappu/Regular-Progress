import sys
def LongestParen(s):
    dp = [0 for _ in range(len(s))]
    maxlen = 0
    for i in range(len(s)):
        if s[i]==')' and i-1>=0 and s[i-1]=='(':
            print("Got it there")
            dp[i] = dp[i-2]+2 if i>2 else 2
        elif s[i]==')' and s[i-1]==')':
            chk  = i-dp[i-1]-1
            if chk>=0 and s[chk] == '(':
                key = i - dp[i-1]-2
                if key >= 0:
                    dp[i] = dp[i-1] + dp[key]+2
                else:
                    dp[i] = dp[i-1] +2
        maxlen = max(maxlen,dp[i])
    return maxlen
if __name__=="__main__":
    s =")("
    print(LongestParen(s))

