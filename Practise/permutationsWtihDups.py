from collections import Counter
import timeit
def permutationsDups(str):
    count = Counter(str)
    arrangements = []
    perform_permut(str,count,arrangements)
    return arrangements
def perform_permut(str,count,arrangements,s=""):
    if len(s) == len(str):
        arrangements.append(s)
        return
    for key in count:
        if count[key]>=1:
            count[key]-=1
            perform_permut(str,count,arrangements,s+key)
            count[key]+=1

if __name__=="__main__":
    s="abcde"
    start = timeit.default_timer()
    print(permutationsDups(s))
    print(timeit.default_timer()-start)

