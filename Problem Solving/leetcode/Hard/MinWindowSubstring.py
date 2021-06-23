from collections import Counter
def MinWindowSubString(s,t):
    if not s or not t:
        return ""
    hash = dict()
    cnt = Counter(t)
    count = 0
    n = len(cnt)
    sol = ""
    w = len(s)+1
    left = right = 0
    while right<len(s):
        i = right
        if s[i] in cnt:
            hash[s[i]] = hash.get(s[i],0)+1
            if hash[s[i]] == cnt[s[i]]:
                count+=1
            while left<=right and count==n:
                if s[left] in cnt:
                    length = right-left
                    if length<w:
                        w = length
                        sol = s[left:right+1]
                    hash[s[left]]-=1
                    if hash[s[left]]<cnt[s[left]]:
                        count-=1
                left+=1
        right+=1
    return sol

if __name__=="__main__":
    s = "aa"
    t = "aa"
    print(MinWindowSubString(s,t))
