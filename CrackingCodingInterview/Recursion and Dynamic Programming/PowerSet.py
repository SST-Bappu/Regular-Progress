def PowerSet(set):
    subsets = [[]]
    i=0
    while i<len(set):
        n = len(subsets)
        j=0
        while j<n:
            subsets.append(subsets[j]+[set[i]])
            j+=1
        i+=1
    return subsets
if __name__=="__main__":
    set = ['a','b','c','d']
    print(PowerSet(set))