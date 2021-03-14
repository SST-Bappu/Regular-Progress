import numpy as np
import sys
import time

#proof that numpy took less time

l = range(1000)
print(sys.getsizeof(5)*len(l))
array = np.arange(1000)
print(array.size*array.itemsize)

#proof that numpy array is convenient and faster

size = 100
l1 = range(size)
l2 = range(size)

a1 = np.arange(size)
a2 = np.arange(size)

start = time.time()
result = [x+y for x,y in zip(l1,l2)]
print ("Python list took ",(time.time()-start)*1000)
start = time.time()
result=a1+a2
print("Numpy array took ",(time.time()-start)*1000)

a=np.zeros((1,1))
print(a)