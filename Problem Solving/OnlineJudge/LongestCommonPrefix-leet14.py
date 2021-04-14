def longestCommonPrefix(strs):
    if len(strs)<=1:
        if not len(strs):
            return ""
        else:
            return strs[0]
    pre = []
    i=0
    while i<len(strs[0]) and i<len(strs[1]) and strs[0][i] == strs[1][i]:
        pre.append(strs[0][i])
        i+=1
    i =2
    while i< len(strs):
        j=0
        if not len(pre):
            return ""
        while j<len(pre) and j<len(strs[i]) and pre[j]==strs[i][j] :
            j+=1
        while len(pre)>j:
            pre.pop()
        i+=1
    return "".join(pre)
if __name__=="__main__":
    strs = ["abab","aba",""]
    print(longestCommonPrefix(strs))
