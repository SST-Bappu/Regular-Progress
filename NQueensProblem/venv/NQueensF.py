import math
x =[0,0]
def place (k,i):
    global x
    for l in range (k):
        j = l+1
        if (x[j]==i) or (abs(x[j]-i)==abs(j-k)):
            return 0
        else:
            return 1

def NQueens(k,n):
    for i in range(1,n+1):
        if place(k,i):
            x[k] = i
            if k==n:
                print(x)
            else:
                NQueens(k+1,n)


n = 8
NQueens(1,n)




