def IsRotation(s1, s2):
    if len(s1)==len(s2) and len(s1)>0:
        s1s1 = s1+s1
        if s1s1.count(s2)>0:
            return True
        else:
            return False
    return False
if __name__=="__main__":
    s1 = "waterbottle"
    s2 = "erbottlewat"
    print(IsRotation(s1,s2))