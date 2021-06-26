def RemoveOccurance(s,part):
    if not part:
        return
    l= len(s)
    while True:
        s = s.replace(part,"")
        if len(s)==l:
            return s
        l = len(s)
    return s
if __name__=="__main__":
    s = "daabcbaabcbc"
    part = "abc"
    print(RemoveOccurance(s,part))
