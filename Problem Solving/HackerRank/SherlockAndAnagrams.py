def Anagrams(str):
    str = list(str)
    Hash = dict()
    for i in range(len(str)):
        for j in range(i,len(str)):
            temp = str[i:j+1]
            temp.sort()
            if Hash.get("".join(temp)):
                val = Hash.get("".join(temp))
                Hash.update({"".join(temp):val+1})
            else:
                Hash.update({"".join(temp):1})
    ang = 0
    print(Hash)
    for i in Hash:
        if Hash.get(i)>1:
            val = Hash.get(i)
            ang+=(val*(val-1))//2
    return ang
if __name__=="__main__":
    str = "cdcd"
    print(Anagrams(str))

