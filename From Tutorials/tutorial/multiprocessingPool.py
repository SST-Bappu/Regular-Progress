from multiprocessing import Pool
import time
def sqr(n):
    return n*n
    sum =0
    for x in range(1000):
        sum+=x*x
    return sum

if __name__=="__main__":
    t1 = time.time()
    p = Pool()
    result = p.map(sqr,range(10000))
    p.close()
    p.join()
    #print("Result is = ",result)
    t2 = time.time()
    t = (t2-t1)
    print (f"Pool took total {t} Seconds")
    t1 = time.time()
    result=[]
    for i in range(10000):
        result.append(sqr(i))

    t = (time.time()-t1)
    print(f"Serial processing took {t} Seconds")


