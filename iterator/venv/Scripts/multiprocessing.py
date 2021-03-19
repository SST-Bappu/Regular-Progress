import time
import multiprocessing

def calculate_sqr(numbers):
    result =[]
    for i in numbers:
        result.append(i*i)
        print("Sqr->",i)
        #time.sleep(0.2)
    print (result)

def calculate_cube(numbers):
    result=[]
    for i in numbers:
        result.append(i * i * i)
        print("Cube->",i)
        #time.sleep(0.2)
    print(result)

if __name__=="__main__":
    arr = range(1,10)
    t = time.time()
    p1 = multiprocessing.Process(target=calculate_sqr, args=(arr,))
    p2 = multiprocessing.Process(target=calculate_cube, args=(arr,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("Total time taken = ",time.time()-t)
