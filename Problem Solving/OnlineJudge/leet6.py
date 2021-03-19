class Solution:
    def ZigZag(self,str,R):
        if len(str)==0 or R>len(str):
            return str
        s=[[] for i in range(R)]
        i=0
        d=-1
        for c in str:
            s[i].append(c)
            if i==0 or i==R-1:
                d*=-1
            i+=d
        for i in range(1,R):
            s[0]+=s[i]
        return ''.join(s[0])
if __name__=="__main__":
    str = "PAYPALISHIRING" #PINALSIGYAHRPI  PAHNAPLSIIGYIR
    result = Solution()
    #res = ""
    res=result.ZigZag(str,4)
    print(res)