class Solution:
    def area_of_two_lines(self,x):
        a = len(x)
        if a<=1:
            return -1
        max_area = 0
        for i in range(a):
            for j in range(i+1,a):
                area = min(x[i],x[j])*(j-i)
                max_area=max(max_area,area)
        return max_area
    def max_Sum_optimized(self,x):
        max_area=0
        i =0
        j=len(x)-1
        while(i<j):
            area = min(x[i],x[j])*(j-i)
            max_area=max(area,max_area)
            if x[i] < x[j]:
                i+=1
            else:
                j-=1
        return max_area


if __name__=="__main__":
    x = [1,8,6,2,5,4,8,3,7]
    result = Solution()
    area=result.max_Sum_optimized(x)
    if area == -1:
        print ("Array is too short")
    else:
        print("The area is = ",area)