import sys


def EliminateMons(dist,speed):
    i=0
    count = 0
    n = len(dist)
    while count<n:
        chk = True
        minV = 0
        for i in range(n):
            if dist[i]==None:
                continue
            dist[i]-=speed[i]
            if dist[minV]==None:
                minV = i
            elif dist[i]<dist[minV]:
                minV = i
            if dist[i]<=0:
                if chk:
                    count+=1
                    dist[i] = None
                    chk = False
                else:
                    return count
        if chk:
            count+=1
            dist[minV] = None
    return count
if __name__=="__main__":
    dist = [4,2,3]
    speed =[2,1,1]
    print(EliminateMons(dist,speed))

