def TrappingRainWater(height):
    left = result = 0
    while left<len(height):
        right = left +1
        cur = 0
        while right<len(height) and height[left]>height[right]:
            cur += height[left]-height[right]
            right+=1
        if right>=len(height):
            left+=1
        else:
            result+=cur
            left = right
    return result
if __name__=="__main__":
    height = [4,2,3]
    print(TrappingRainWater(height))