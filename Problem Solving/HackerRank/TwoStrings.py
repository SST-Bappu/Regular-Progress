from collections import Counter
def TwoStrings(s1,s2):
    cnt = Counter(s1)
    i=0
    while(i<len(s2)):
        if cnt.get(s2[i]):
            return "YES"
        i+=1
    return "NO"
if __name__=="__main__":
    s1 = "hello"
    s2 = "world"
    print(TwoStrings(s1,s2))