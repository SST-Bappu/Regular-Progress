nums = [1,-1,3,4]
n= len(nums)
x = next((i+1 for i, num in enumerate(nums) if num!=i+1),n+1)
print(x)

chk = [1,2]
print(next(enumerate(chk)))