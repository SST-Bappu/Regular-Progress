import multiprocessing
import time

def calcsqr(numbers):
    for i in numbers:
        print("Square - ",i*i)
        time.sleep(1)
def calcube(numbers):
    for i in numbers:
        print("Cube - ",i*i*i)
        time.sleep(2)

if __name__=="__main__":
    x = [2,3,8,9]
    p1 = multiprocessing.Process(target=calcsqr,args=(x,))
    p2 = multiprocessing.Process(target=calcube,args=(x,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print("Done")