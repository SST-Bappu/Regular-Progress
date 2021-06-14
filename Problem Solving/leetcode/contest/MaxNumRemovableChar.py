from collections import defaultdict
def RemovableChar(s,p,removable):
    s = list(s)
    k=0
    while k<len(removable):
        j=0
        while j<k:
            if removable[j]<removable[k]:
                removable[k]-=1
            j+=1
        s.pop(removable[k])
        i = 0
        for c in s:
            if c==p[i]:
                i+=1
            if i>=len(p):
                break
        if not (i>=len(p)):
            return k
        k+=1
    return k
if __name__=="__main__":
    s = "qobftgcueho"
    p = "obue"
    removable = [5, 3, 0, 6, 4, 9, 10, 7, 2, 8]
    print(RemovableChar(s,p,removable))


