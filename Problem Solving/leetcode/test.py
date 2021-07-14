from collections import Counter
nums = [1,2,2]
cnt = Counter(nums)
for key in cnt:
    print(cnt[key])