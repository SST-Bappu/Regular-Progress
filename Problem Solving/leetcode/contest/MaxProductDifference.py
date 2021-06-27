def ProductDiff(nums):
    nums.sort()
    left = nums[-1]*nums[-2]
    right = nums[0]*nums[1]
    return left-right
if __name__=="__main__":
    print(ProductDiff([4,2,5,9,7,4,8]))