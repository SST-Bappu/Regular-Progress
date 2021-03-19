class Solution:
    def findMedianSortedArrays(self,num1,num2):
        k= len(num1)
        l= len(num2)
        result=[]
        i = j = 0
        while True:
            if i<k and j<l:
                if num1[i]>num2[j]:
                    result.append(num2[j])
                    j+=1
                else:
                    result.append(num1[i])
                    i+=1
            elif i<k:
                result.append(num1[i])
                i+=1
            elif j<l:
                result.append(num2[j])
                j+=1
            else:
                break
        length = len(result)
        f = length//2
        if (length%2==0):
            ans = (result[f]+result[f-1])/2
            return ans
        else:
            return result[f]


if __name__=="__main__":
    num1 = [2]
    num2 = []
    result = Solution()
    print(result.findMedianSortedArrays(num1,num2))