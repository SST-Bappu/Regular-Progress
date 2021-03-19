from collections import Counter
def ReplaceSpace(str):
    n = len(str)
    while(n):
        if str[n-1]==' ':
            str.pop(n-1)
            n-=1
        else:
            break
    cnt = Counter(str)
    index = len(str)+cnt[' ']*2
    str_array= [None]*index
    for i in range(len(str)-1,-1,-1):
        if str[i]==" ":
            str_array[index-1]='0'
            str_array[index-2]='2'
            str_array[index-3]='%'
            index-=3
        else:
            str_array[index-1]=str[i]
            index-=1
    return str_array

if __name__=="__main__":
    str = "This is just a test case.   "
    str = list(str)
    str = ReplaceSpace(str)
    str1 = ""
    str1=str1.join(str)
    print(str1)

