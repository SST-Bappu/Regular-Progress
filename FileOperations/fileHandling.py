file = open('data','r') #rb - read Binary,
# print(file.read())
# print(file.readline())
file1 = open('abc','w') #a - append(to add data in existing file)
sum = 0
for line in file:
    sum+=int(line)
print(sum)
