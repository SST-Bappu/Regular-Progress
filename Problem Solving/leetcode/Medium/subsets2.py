from collections import Counter
def subsets(nums):
    cnt = Counter(nums)
    result = [[]]
    for key in cnt:
        cur = []
        n = len(result)
        i = 0
        while i<n:
            result.append(result[i]+[key])
            if cnt[key]>1:
                cur.append(result[i]+[key])
            i+=1
        cnt[key]-=1
        i=0
        while cnt[key]:
            n = len(cur)
            while i<n:
                result.append(cur[i]+[key])
                cur.append(cur[i]+[key])
                i+=1
            cnt[key]-=1
    return result
if __name__=="__main__":
    nums = [0]
    print(subsets(nums))
