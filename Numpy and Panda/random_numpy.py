from numpy import random
import numpy as np
x = random.randint(100)
# print(x)

x  = random.randint(100,size=5) #Generate an 1D array of size 5
# print(x)
x  = random.randint(100,size=(3,5)) #Generate a 2Darray of size (3,5)
# print(x)

x = random.rand() #Generate a random float between 0 and 1
# print(x)

x = random.rand(5) #Generate a 1-D array containing 5 random floats
# print(x)

x = random.rand(5,3)
#print(x)

x = random.choice([3,5,4,7,8,10])
# print(x)

x = random.choice([3,5,4,7,8,10],size=5)
#print(x)

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.4, 0.2], size=(100)) #random number with probability function
# print(x)

nums = [3,5,4,7,8,10]
random.shuffle(nums)
# print(nums)

arr = np.array([3,5,4,7,8,10])
x = random.permutation(arr)
print(x)
