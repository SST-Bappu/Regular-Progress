def checkArmstrong(num):
    n1 = n2 = num
    c = 0
    while n1:
        c+=1
        n1//=10
    sum = 0
    while n2:
        sum+=pow(n2%10,c)
        n2//=10
    if sum==num:
        print(num,"is an Armstrong number")
    else:
        print(f"{num} is not an Armstrong number")
def SumSeries(n):
    sum = 0.0
    for i in range(1,n+1):
        sum+=1.0/i
    return sum



if __name__=="__main__":
    str = "Hello World"
    Rstr = str[::-1]
    print(Rstr)