class Solution:
    def trapped(self,x):
        total = 0
        max_L = 0
        for i in range(len(x)):
            max_R = 0
            if i>0:
                max_L=max(max_L,x[i-1])
            for j in range (i+1,len(x)):
                max_R=max(max_R,x[j])
            water_blog = min(max_R,max_L)-x[i]
            if water_blog>0:
                total+= water_blog
        return total
    def trap_optimized(self,x):
        total = 0
        max_L = 0
        max_R = 0
        i = 0
        j = len(x)-1
        for item in x: #while(i<=j)
            if max_L<=max_R:
                if x[i]<=max_L:
                    total+=max_L-x[i]
                else:
                    max_L = x[i]
                i+=1
            else:
                if x[j]<=max_R:
                    total+=max_R-x[j]
                else:
                    max_R = x[j]
                j-=1
        return total


if __name__=="__main__":
    result = Solution()
    x =[0,1,0,2,1,0,3,1,0,1,2]
    y = [4,2,0,3,2,5]
    print(result.trapped(x))
    print(result.trap_optimized(x))




