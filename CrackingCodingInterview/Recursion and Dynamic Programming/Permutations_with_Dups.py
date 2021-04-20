#This solution came from the previous permutations solution, here I just use set instead of list.
#The problem is here I'm calculating all the possible permutations which is a bit tedious.
#So in the next solution I'll try to ignore the additinoal solutions that may take part. For exaple, if my input is ="aac".As there are 3 letters this
#solution will calculate 6 permutation I mean 6 strings. But if we look closer there only 3 permutations possible. So in the next solution we only take
#those 3, ignoring all the possible 6.
from collections import Counter
def get_perms_2(string):
    result = set()
    get_perms_inner_2(" ", string, result)
    return result

def get_perms_inner_2(prefix, remainder, result):
    if len(remainder) == 0:
        result.add(prefix)
    length = len(remainder)
    for i in range(length):
        before = remainder[:i]
        after = remainder[i + 1 :]
        c = remainder[i]
        get_perms_inner_2(prefix + c, before + after, result)
def insert_char_at(c,word,i):
    first = word[:i]
    last = word[i:]
    return first+c+last
#This is the optimized one
def Permutations_dups_optimized(s):
    char_count = Counter(s)
    result = []
    get_string(char_count,"",len(s),result)
    return result

def get_string(char_count,prefix,remaining,result):
    if remaining==0:
        result.append(prefix)
        return
    for char in char_count:
        count = char_count[char]
        if count>0:
            char_count[char]-=1
            get_string(char_count,prefix+char,remaining-1,result)
        char_count[char] = count
if __name__=="__main__":
    s= "aacc"
    print(Permutations_dups_optimized(s))