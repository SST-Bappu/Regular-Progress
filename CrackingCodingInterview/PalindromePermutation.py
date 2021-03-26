from collections import Counter
def PalindromePermut(str):
    cnt = Counter(str)
    chk = 0
    l = len(str)
    for i in cnt:
        if cnt[i]%2!=0 and l%2==0:
            return False
        elif cnt[i]%2!=0 and l%2!=0 and chk>=1:
            return False
        elif cnt[i]%2!=0 and l%2!=0:
            chk+=1
    return True

if __name__=="__main__":
    str = "Tact Coaoot"
    str = str.lower()
    str = list(str)
    n = len(str)
    i=0
    while(i<n):
        if not (str[i]>= 'a' and str[i]<='z'):
            str.pop(i)
            n-=1
        i+=1
    print(PalindromePermut(str))

