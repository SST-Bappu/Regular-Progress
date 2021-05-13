import copy
import timeit
def StringPermutations(s):
    s=list(s)
    per_strings = []
    Permutations(s,per_strings)
    return per_strings
def Permutations(s,per_strings,level=0):
    if level>= len(s)-1:
        per_strings.append("".join(s))
        return
    i=0
    while i< len(s):
        if i>=level:
            cur = copy.deepcopy(s)
            cur[i],cur[level] = cur[level],cur[i]
            Permutations(cur,per_strings,level+1)
        i+=1
#A more optimized way to get permutations done
def get_perms(s):
    if s==None:
        return None
    permutations = []
    if len(s)==0:
        permutations.append(" ")
        return permutations
    first = s[0]
    remainder = s[1:]
    words = get_perms(remainder)
    for word in words:
        i = 0
        for _ in word:
            s = insert_char_at(first,word,i)
            permutations.append(s)
            i+=1
    return permutations
def insert_char_at(c,word,i):
    first = word[:i]
    last = word[i:]
    return first+c+last


#One more solution, better than first one but not faster than the optimized one
def get_perms_2(string):
    result = []
    get_perms_inner_2(" ", string, result)
    return result

def get_perms_inner_2(prefix, remainder, result):
    if len(remainder) == 0:
        result.append(prefix)
    length = len(remainder)
    for i in range(length):
        before = remainder[:i]
        after = remainder[i + 1 :]
        c = remainder[i]
        get_perms_inner_2(prefix + c, before + after, result)
if __name__=="__main__":
    s = "abc"
    # start = timeit.default_timer()
    # result = StringPermutations(s)
    # print(result)
    # print(timeit.default_timer()-start)
    start = timeit.default_timer()
    result = get_perms(s)
    print(result)
    print(timeit.default_timer()-start)
    # start = timeit.default_timer()
    # result = get_perms_2(s)
    # print(result)
    # print(timeit.default_timer()-start)