def fibo():
    a,b=0,1
    while 1:
        yield a
        a,b = b,a+b

for i in fibo():
    if i>30:
        break
    print(i)