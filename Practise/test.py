from collections import Counter
str = "aaabbcded"
count = Counter(str)
print(count)
for key in count:
    print(count[key])