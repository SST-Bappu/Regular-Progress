def ReverseInteger(num):
    chk =0
    if num<0:
        chk =1
        num*=-1
    res = 0
    while(num>0):
        res*=10
        res+=num%10
        num//=10
    if (res > pow(2,31)):
        return 0
    return res if chk==0 else res*(-1)
def RecursiveReverse(num):
    if num==0:
        return 0
    return 10*num%10+RecursiveReverse(num//10) * (-1) if num<0 else 1
if __name__=="__main__":
    print(ReverseInteger(-123))
