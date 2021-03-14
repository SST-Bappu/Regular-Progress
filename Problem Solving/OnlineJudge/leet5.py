class Solution:
    def longestPalindrome(self,str):
        maxLength = 0
        left = 0
        list =[]
        while(len(str)-left)>maxLength:
            right = len(str)-1
            while(left<=right):
                l = left
                r = right
                cnt = 0
                while(l<=r and str[l]==str[r]):
                    cnt+=2
                    if l == r:
                        cnt -= 1
                    l += 1
                    r -= 1
                if (l>=r and cnt>maxLength):
                    list.clear()
                    for i in range(left,right+1):
                        list.append(str[i])
                    maxLength=cnt
                    break
                right-=1
            left+=1
        rslt = ""
        return rslt.join(list)
    def Optimized(self,str):
        #str = list(str)
        start = 0
        end = 0
        if len(str)==0:
            return ""
        cnt = 0
        for i in range(len(str)):
            len1 = self.ExpandFromMiddle(str,i,i)
            len2 = self.ExpandFromMiddle(str,i,i+1)
            l = max(len1,len2)
            if l>1: #To check how many Palindroms are there
                cnt+=1
            if l>(end-start):
                start = i-(l-1)//2
                end = i+l//2
        print("Total Palindroms is = ",cnt)
        return str[start:end+1]
    def ExpandFromMiddle(self,str,left,right):
        if left>right:
            return 0
        while(left>=0 and right<len(str) and str[left]==str[right]):
            left-=1
            right+=1
        return right-left-1



if __name__=="__main__":
    str = "aacabdkaca"
    str = str.lower()
    s = list(str)
    result = Solution()
    print(result.Optimized(s))





