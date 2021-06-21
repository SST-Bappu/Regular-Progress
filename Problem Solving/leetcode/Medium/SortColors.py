from collections import Counter
def SortColors(nums):
    count = Counter(nums)
    print(count)
    index = 0
    for i in range(3):
        while count[i]:
            print(i)
            nums[index] = i
            count[i]-=1
            index+=1
if __name__=="__main__":
    nums = [2,0]
    SortColors(nums)
    print(nums)