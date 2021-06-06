def ReducOperations(nums):
    smallest = min(nums)
    count = 1
    chk = False
    for i in nums:
        if i>smallest:
            count+=1
            chk = True
    return count if chk else 0
if __name__=="__main__":
    nums = [1,1,2,2,3]
    print(ReducOperations(nums))