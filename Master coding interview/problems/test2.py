string = "12 apples, 10 oranges, 2 bananas"

news = string.split(',')
print(news)
sum = 0
for s in news:
    x = s.split()
    sum+=int(x[0])
print(sum)