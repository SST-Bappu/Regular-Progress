import timeit
class Solution:
    def findAlmostPalindrom(self,str):
        i = 0
        j = len(str)-1
        cnt = 0
        while(i<j):
            if str[i]==str[j]:
                i+=1
                j-=1
            elif cnt<1:
                if str[i]==str[j-1]:
                    j-=1
                elif str[i+1]==str[j]:
                    i+=1
                else:
                    return False
                cnt+=1
            else:
                return False
        return True

if __name__=="__main__":
    str = "Race #=?a/ Car"
    now = timeit.default_timer()
    str = str.lower()
    s = list(str)
    i=0
    n=len(s)
    while (i < n):
        if not (s[i] >= 'a' and s[i] <= 'z'):
            s.pop(i)
            n -= 1
        else:
            i += 1
    rslt = Solution()
    print(rslt.findAlmostPalindrom(s))
    time = timeit.default_timer() - now
    print(f"Required Run Time = {time*1000} seconds")

