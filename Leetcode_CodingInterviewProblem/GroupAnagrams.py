def GroupAnagrams(Anagrams):
    hash=dict()
    for i in Anagrams:
        item = sorted(i)
        item = "".join(item)
        if hash.get(item):
            hash[item].append(i)
        else:
            hash[item] = [i]
    return [x for x in hash.values()]

if __name__=="__main__":
    anagrams = ["eat","tea","tan","ate","nat","bat"]
    print(GroupAnagrams(anagrams))