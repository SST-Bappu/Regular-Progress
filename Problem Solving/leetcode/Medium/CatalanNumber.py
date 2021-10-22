import math


def TotalBinarySearchTree(n):
    memo = [1,1]
    for i in range(2,n+1):
        cur = 0
        for j in range(math.ceil(i/2)):
            cur += memo[j]*memo[i-j-1]
            if j+1==i//2:
                keep = cur
        memo.append(cur+keep)
    return memo[-1]

if __name__=="__main__":
   print(TotalBinarySearchTree(2))