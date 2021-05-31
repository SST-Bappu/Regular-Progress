def TrappingRainWater(height):
    left = right = total = i = 0
    j = len(height)-1
    while i<=j:
        if left<=right:
            if height[i]<=left:
                total+=left-height[i]
            else:
                left = height[i]
            i+=1
        else:
            if height[j]<=right:
                total += right-height[j]
            else:
                right = height[j]
            j-=1
    return total
if __name__=="__main__":
    height = [4,2,0,3,2,5]
    print(TrappingRainWater(height))