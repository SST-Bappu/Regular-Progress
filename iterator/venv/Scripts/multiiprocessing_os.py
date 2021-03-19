import os
from multiprocessing import Process,current_process

def sqr(number):
    result = number*number
    process_id = os.getpid()
    print(f"The process id is = {process_id}")
    print (f"{number} square to {result}")


if __name__=="__main__":
    numbers =[1,2,3,4]
    processes=[]
    for number in numbers:
        process = Process(target=sqr,args=(number,))
        processes.append(process)
        process.start()