def BinarySum_mine(bin1,bin2):
    n = len(bin1)
    Decim_bin1 = 0
    cnt=0
    for i in range(n-1,-1,-1):
        Decim_bin1+= int(bin1[i])*pow(2,cnt)
        cnt+=1
    n = len(bin2)-1
    Decim_bin2=0
    cnt = 0
    for i in range(n,-1,-1):
        Decim_bin2+=int(bin2[i])*pow(2,cnt)
        cnt+=1
    sum = Decim_bin1+Decim_bin2
    print(sum)
    newlen = max(len(bin1),len(bin2))
    BinSum=""
    chk = False
    while newlen>=0:
        if sum>=pow(2,newlen):
            sum-=pow(2,newlen)
            BinSum+='1'
            chk = True
        elif chk:
            BinSum+='0'
        newlen-=1
    return BinSum
def BinarySum(bin1,bin2): #More Optimized
    i , j = len(bin1)-1,len(bin2)-1
    result=[]
    carry = 0
    while(i>=0 or j>=0):
        total = carry
        if i>=0:
            total += int(bin1[i])
            i-=1
        if j>=0:
            total+= int(bin2[j])
            j-=1
        result.append(str(total%2))
        carry = total//2
    if carry:
        result.append(str(carry))
    return ''.join(reversed(result))



if __name__=="__main__":
    bin1 = "1011"
    bin2 = "1111"
    print(BinarySum(bin1,bin2))
