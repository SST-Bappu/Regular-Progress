def strstr(haystack,needle):
    if not len(needle):
        return 0
    i=0
    while i<len(haystack):
        if haystack[i]==needle[0]:
            j = 0
            keep = i
            map = None
            while i<len(haystack) and j<len(needle) and needle[j]==haystack[i]:
                if not map and i>keep and haystack[i]==needle[j]:
                    map = i
                j+=1
                if j==len(needle):
                    return keep
                i+=1
            if not map:
                continue
            if len(haystack)-map>=len(needle):
                i = map
            else:
                return -1
        else:
            i+=1
    return -1

def strStr_opt(self, haystack: str, needle: str) -> int:
    if not len(needle):
        return 0
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i + len(needle)] == needle:
            return i
    return -1
if __name__=="__main__":
    print(strstr("a","a"))
