def MissingNumber(Numbers):
    n = len(Numbers)
    TotalSum = n*(n+1)/2
    cursum = sum(Numbers)

    return TotalSum-cursum

if __name__=="__main__":
    list = [9,6,4,2,3,5,7,0,1]
    print(int(MissingNumber(list)))
