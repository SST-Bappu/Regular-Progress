from collections import deque
def TowerOfHanoi(a,b,c,n):
    if n==0:
        return
    TowerOfHanoi(a,c,b,n-1)
    c.append(a.pop())
    TowerOfHanoi(b,a,c,n-1)
if __name__=="__main__":
    a = [10,8,6,3]
    b=[]
    c=[]
    TowerOfHanoi(a,b,c,4)
    print(c)