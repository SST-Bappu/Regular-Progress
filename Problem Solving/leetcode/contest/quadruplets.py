def countQuadruplets(nums):
    result = []
    for i in range(nums[0]+1):
        count(result,nums,i,0)
    return len(result)

def count(result,nums,num,i,cur=[]):
    if i==len(nums)-1:
        cur.append(nums[i])
        if sum(cur) == nums[len(nums)-1]:
            result.append(cur)
        return
    if num>=nums[i+1]:
        return

    count(result,nums,num+1,i+1)

if __name__=="__main__":
    nums = [1,1,1,3,5]
    result = countQuadruplets(nums)
    for row in result:
        print(row)
