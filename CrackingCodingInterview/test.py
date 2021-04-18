import copy
s ="strings"
s2 =copy.deepcopy(s)
print(s2)
p = "c"
first = p[0]
last = p[1:]
print(first)
print(len(last))
for word in last:
    for s in word:
        print(s)
print(last[:0])
