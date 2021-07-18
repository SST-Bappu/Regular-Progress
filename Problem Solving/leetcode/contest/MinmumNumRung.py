import math


def MinnumRung(rungs,dist):
    cur = 0
    cnt = 0
    i = 0
    while i<len(rungs):
        if (rungs[i]-cur)>dist:
            cnt+= math.ceil((rungs[i]-cur-dist)/dist)

        cur=rungs[i]
        i+=1
    return cnt
if __name__=="__main__":
    rungs = [3,4,6,7]
    print(MinnumRung(rungs,2))