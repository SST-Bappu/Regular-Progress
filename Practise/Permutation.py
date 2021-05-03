import copy
import timeit
def permutation(str):
   arrangements = []
   str = list(str)
   perform_permut(str,arrangements,0)
   return arrangements
def perform_permut(str,arrangements,n):
    if n==len(str)-1:
        arrangements.append("".join(str))
        return
    i = n
    while i<len(str):
        str1 = copy.deepcopy(str)
        if i>n:
            str1[i],str1[n] = str1[n],str1[i]
        perform_permut(str1,arrangements,n+1)
        i+=1

def permutations_m2(str):
    arrangements =[]
    perform_permut_m2(str,arrangements)
    return arrangements
def perform_permut_m2(str,arrangements,n=0,s=""):
    if n==len(str):
        arrangements.append(s)
        return
    i=0
    while i<=n:
        s_new = arrange_m2(i,str[n],s)
        perform_permut_m2(str,arrangements,n+1,s_new)
        i+=1
def arrange_m2(i,c,s):
    left = s[i:]
    right = s[:i]
    return left+c+right

def permutations_m3(str):
    arrangements=[]
    perform_permut_m3("",str,arrangements)
    return arrangements
def perform_permut_m3(prefix,remainder,arrangements):
    l = len(remainder)
    if l==0:
        arrangements.append(prefix)
        return
    for i in range(l):
        before = remainder[:i]
        after = remainder[i+1:]
        c = remainder[i]
        perform_permut_m3(prefix+c,before+after,arrangements)
if __name__=="__main__":
    str = "abcdefgh"
    start = timeit.default_timer()
    result = permutation(str)
    print(timeit.default_timer()-start)
    start = timeit.default_timer()
    result= permutations_m2(str)
    print(timeit.default_timer()-start)
    start = timeit.default_timer()
    result = permutations_m3(str)
    print(timeit.default_timer()-start)
