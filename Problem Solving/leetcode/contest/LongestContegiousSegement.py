def LongestContegiousSegment(s):
    zeroes = ones = 0
    i= 0
    n = len(s)
    while i<n:
        z=o=0
        if s[i]=='0':
            while i<n and s[i]=='0':
                z+=1
                i+=1
            zeroes = max(z,zeroes)
        elif s[i]=='1':
            while i<n and s[i]=='1':
                o+=1
                i+=1
            ones= max(ones,o)
    return ones>zeroes
if __name__=="__main__":
    s = "110100010"
    print(LongestContegiousSegment(s))