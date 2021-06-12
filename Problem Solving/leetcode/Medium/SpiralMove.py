def SpiralMove(nums):
    m = len(nums)
    n = len(nums[0])
    k= 0
    result = []
    total = m*n
    while total:
        i = k
        j = k
        chk = False
        while j<n-k-1:
            result.append(nums[i][j])
            total-=1
            chk = True
            j+=1
        while i<m-k:
            result.append(nums[i][j])
            total -= 1
            i+=1
        if chk:
            j-=1
        if i>k:
            i-=1
        while j>k and i>k:
            result.append(nums[i][j])
            total -= 1
            j-=1

        while chk and i>k:
            result.append(nums[i][j])
            total -= 1
            i-=1
        k+=1
    return result
if __name__=="__main__":
    nums = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    # nums = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
    # nums = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
    # nums = [[7],[9],[6]]
    print(SpiralMove(nums))