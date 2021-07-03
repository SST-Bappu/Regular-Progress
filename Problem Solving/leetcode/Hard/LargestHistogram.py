#Brute Force
def LargestHistogram(nums):
    i=0
    result = 0
    n = len(nums)
    while i<n:
        j=0
        point = 0
        while j<n:
            if nums[j]<nums[i]:
                if j>i:
                    sol = (j-point) * nums[i]
                    result = max(sol,result)
                    break
                else:
                    point = j+1
            j+=1
        if j==n:
            result = max(result,(j-point)*nums[i])
        i+=1
    return result
#More optimized way
def LargestRectHisto(heights):
    n = len(heights)
    left =[]
    right = []
    for i in range(n):
        left.append(0)
        right.append(0)
    left[0] = -1
    right[-1] = n
    for i in range(1,n):
        point = i-1
        while point>=0 and heights[point]>=heights[i]:
            point = left[point]
        left[i] = point
    for i in reversed(range(0,n-1)):
        point = i+1
        while point<n and heights[point]>=heights[i]:
            point = right[point]
        right[i] = point
    result = 0
    print(right)
    print(left)
    for i in range(n):
        result = max(result, (right[i]-left[i]-1)*heights[i])
    return result


if __name__=="__main__":
    nums = [2,1,5,6,2,3]
    print(LargestRectHisto(nums))
