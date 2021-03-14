import time
def time_it(func):
    def wrapper(*args,**kwargs):
        print("wrapper started at",time.time())
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        totalTime=(end-start)*1000
        print(func.__name__+" took "+str(totalTime)+" miliseconds")
        return result
    return wrapper

@time_it
def calculate_sqr(numbers):
    result =[]
    for i in numbers:
        result.append(i*i)
    print("calculate_sqr is done")
    return result

@time_it
def calculate_cube(numbers):
    result=[]
    for i in numbers:
        result.append(i*i*i)
    print("calculate_cube is done")
    return result

#if "__name__"=="__main__":
arr = range(1,1000)
out_sqr=calculate_sqr(arr)
out_cube=calculate_cube(arr)
print(out_sqr)
print(out_cube)
