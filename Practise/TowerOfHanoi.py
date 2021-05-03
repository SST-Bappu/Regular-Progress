def TowerOfHanoi(a,b,c,n):
    if n==0:
        return 0
    TowerOfHanoi(a,c,b,n-1)
    c.append(a.pop())
    TowerOfHanoi(b,a,c,n-1)

if __name__=="__main__":
    a = [1,2,3]
    b=[]
    c=[]
    TowerOfHanoi(a,b,c,len(a))
    print(c)