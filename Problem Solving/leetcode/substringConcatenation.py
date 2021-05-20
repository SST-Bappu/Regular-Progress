from collections import Counter
def findSubstring(s,words): #It works but too slow, we don't necessarily need the permutation to solve this problem
    permutedWords = wordPermutations(words)
    hash = {}
    for i in range(len(permutedWords)):
        if not hash.get(permutedWords[i][0]):
            hash[permutedWords[i][0]] = [permutedWords[i]]
        else:
            hash[permutedWords[i][0]].append(permutedWords[i])
    result = []
    i=0
    n= len(permutedWords[0])
    while (len(s)-i)>=n:
        if hash.get(s[i]):
            for word in hash[s[i]]:
                if s[i:i+n]==word:
                    result.append(i)
                    break
        i+=1
    return result

def wordPermutations(words):
    hash = Counter(words)
    n=0
    for word in words:
        n+=len(word)
    arrangements =[]
    arrange("",hash,n,arrangements)
    return arrangements

def arrange(pre,hash,n,arrangements):
    if len(pre)==n:
        arrangements.append(pre)
        return
    for key in hash:
        if hash[key]>0:
            hash[key]-=1
            arrange(pre+key,hash,n,arrangements)
            hash[key]+=1

def findSubstring_optimized(s,words): #This is the optimized one and indeed a nice solution
    hash = Counter(words)
    str_n = len(s)
    word_n = len(words[0])
    sub_n = len(words)*word_n
    result = []
    for i in range(min(word_n,(str_n-sub_n+1))):
        findIndex(s,i,i,word_n,sub_n,str_n,hash,result)
    return result
def findIndex(s,keep,start,word_n,sub_n,n,hash,result):
    cur_hash={}
    while start+word_n<=n:
        word = s[start:start + word_n]
        start+=word_n
        if not hash.get(word):
            keep=start
            cur_hash.clear()
            continue
        cur_hash[word] = cur_hash[word]+1 if cur_hash.get(word) else 1
        while cur_hash[word]>hash[word]:
            cur_hash[s[keep:keep+word_n]]-=1
            keep+=word_n
        if start-keep == sub_n:
            result.append(keep)
            cur_hash[s[keep:keep+word_n]]-=1
            keep+=word_n

if __name__=="__main__":
    words = ["word","good","best","word"]
    s = "wordgoodgoodgoodbestword"
    print(findSubstring_optimized(s,words))