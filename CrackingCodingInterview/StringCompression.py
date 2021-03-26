from collections import Counter
def StringCompression(s):
    list = []
    i=0
    while i<len(s):
        list.append(s[i])
        c = s[i]
        cnt = 0
        while (s[i]==c):
            i+=1
            cnt+=1
            if i>=len(s):
                break
        c = "%s"% cnt
        list.append(c)
    return list if len(list)<len(s) else s
if __name__=="__main__":
    str = "aabcccccaaa"
    str = list(str)
    d= ""
    str = StringCompression(str)
    d=d.join(str)
    print(d)