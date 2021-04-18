import copy
list = [[],[2,4]]
i=0
n = len(list)
while i<n:
    list.append(list[i]+[6])
    i+=1
print(list)
listtest = copy.copy(list)
listtest[3].append(10)
print(list)
print(listtest)
print(4>>1)