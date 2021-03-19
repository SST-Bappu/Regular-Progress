import time
import threading

def calculate_sqr(numbers):
    result =[]
    for i in numbers:
        result.append(i*i)
        print("Sqr->",i)
        time.sleep(0.2)
    print (result)

def calculate_cube(numbers):
    result=[]
    for i in numbers:
        result.append(i * i * i)
        print("Cube->",i)
        time.sleep(0.2)
    print(result)

#if "__name__"=="__main__":
arr = range(1,5)
t = time.time()
t1 =threading.Thread(target=calculate_sqr, args=(arr,))
t2 =threading.Thread(target=calculate_cube, args=(arr,))
t1.start()
t2.start()
t1.join()
t2.join()
print("Total time taken = ",time.time()-t)
