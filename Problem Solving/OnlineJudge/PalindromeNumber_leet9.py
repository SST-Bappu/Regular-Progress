def PalindromeNumber(num):
    if num<0:
        return False
    hold=num
    rev=0
    while(hold>0):
        rev*=10
        rev+=hold%10
        hold//=10
    return True if rev==num else False
def MoreOptimized(num):
    if num<0 or (num%10==0 and num!=0):
        return False
    right = 0
    while(right<num):
        right*=10
        right+=num%10
        num//=10

    return right==num or num==right//10
if __name__=="__main__":
    print(MoreOptimized(-101))
