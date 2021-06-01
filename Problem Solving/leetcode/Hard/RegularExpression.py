def RegularExpression(s,p):
    DP = {}
    def DFS(i,j):
        if DP.get((i,j)):
            return DP[(i,j)]
        if i>=len(s) and j>=len(p):
            return True
        if j>= len(p):
            return False
        match = i<len(s) and (s[i]==p[j] or p[j]=='.')
        if j+1<len(p) and p[j+1] == '*':
            DP[(i,j)] = DFS(i,j+2) or (match and DFS(i+1,j))
            return DP[(i,j)]
        if match:
            DP[(i,j)] = DFS(i+1,j+1)
            return DP[(i,j)]
        DP[(i,j)] = False
        return DP[(i,j)]
    return DFS(0,0)

if __name__=="__main__":
    s = "aasdfasdfasdfasdfas"
    p ="aasdf.*asdf.*asdf.*asdf.*s"
    print(RegularExpression(s,p))

