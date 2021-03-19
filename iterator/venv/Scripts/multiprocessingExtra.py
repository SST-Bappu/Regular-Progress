import multiprocessing
result_sqr=[]
def sqr(numbers):
    global result_sqr
    for i in numbers:
        print("Square of "+str(i)+" is ="+str(i*i))
        result_sqr.append(i)
    print(result_sqr)

if __name__=="__main__":
    arr=[1,2,3,4,5,6,7]
    p1 = multiprocessing.Process(target=sqr,args=(arr,))
    p1.start()
    p1.join()
    print(result_sqr)
