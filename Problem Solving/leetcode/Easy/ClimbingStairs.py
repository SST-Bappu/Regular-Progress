def ClimbingStairs(n):
    stairs = [0 for _ in range(n+1)]
    stairs[0] = 1
    for i in range(1,n+1):
        if i==1:
            stairs[i] = stairs[i-1]
            continue
        stairs[i] = stairs[i-1] + stairs[i-2]
    return stairs[n]

if __name__=="__main__":
    print(ClimbingStairs(3))
