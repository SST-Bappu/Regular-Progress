def StringToInteger(s):
    res =0
    chk = False
    leading = False
    op = False
    for c in s:
        if c>= '0' and c<='9':
            res *=10
            res+=int(c)
            leading = True
        elif (c=='-' or c=='+') and not(leading):
            if op:
                return 0
            op = True
            if c=='-':
                chk = True
            leading = True
        elif c==" ":
            if leading:
                break
            continue
        else:
            if leading or c=='.':
                break
            else:
                return 0
    if res>=pow(2,31):
        if chk:
            return -pow(2,31)
        else:
            return pow(2,31)-1
    return -res if chk else res

if __name__=="__main__":
    s = "   +0 123"
    print(StringToInteger(s))