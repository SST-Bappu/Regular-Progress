from functools import reduce

def div_decorat(func):
    def wrap_div(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return wrap_div

@div_decorat
def divis(a,b):
    return a/b



result = divis(2,4)
print(result)
nums = [3,2,6,8,4,7,9]
evens = list(filter(lambda n:n%2==0,nums))
print(evens)
sum = reduce(lambda a,b:a+b,evens)
print(sum)