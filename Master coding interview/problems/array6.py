#Longest NonRepeatative SubString
class Solution:
    def LongestSubString(self,str):
        substr =[]
        i=0
        maxsubstr = 0
        while i < len(str):
            substr.append(str[i])
            cnt=1
            for j in range(i+1,len(str)):
                if str[j] not in substr:
                    substr.append(str[j])
                    cnt+=1
                else:
                    substr.clear()
                    break
            maxsubstr = max(maxsubstr, cnt)
            i+=1
        return maxsubstr
    def LongestSubString_Optimezed(self,str): #Sliding Window Technique
        hashtable= dict()
        substr = 0
        cnt = 0
        left = 0
        for i in range(len(str)):
            val = hashtable.get(str[i])
            if val is None or int(val)<left:
                hashtable.update({str[i]:i})
                cnt+=1
            else:
                left = int(val)+1
                cnt = i-int(val)
                hashtable.update({str[i]:i})

            substr=max(substr,cnt)
        return substr


if __name__=="__main__":
    str = "dvdf"
    x = list(str)
    result = Solution()
    print(result.LongestSubString(x))
    print(result.LongestSubString_Optimezed(x))