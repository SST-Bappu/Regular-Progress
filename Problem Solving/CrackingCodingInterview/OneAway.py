def OneAway(str1,str2):
    if len(str1)==len(str2):
        return OneReplace(str1,str2)
    elif len(str1)+1==len(str2):
        return OneInsert(str1,str2)
    elif len(str1)-1==len(str2):
        return OneInsert(str2,str1)
    else:
        return False
def OneReplace(str1,str2):
    chk = False
    for i in range(len(str1)):
        if str1[i]!=str2[i]:
            if chk:
                return False
            chk = True
    return True
def OneInsert(str1,str2):
    i = 0
    j = 0
    while (i<len(str1) and j<len(str2)):
        if str1[i]!=str2[j]:
            if i!=j:
                return False
            j+=1
        else:
            i+=1
            j+=1
    return True

if __name__=="__main__":
    str1 = "apple"
    str2 = "aple"
    str1 = list(str1)
    str2 = list(str2)
    print(OneAway(str1,str2))

