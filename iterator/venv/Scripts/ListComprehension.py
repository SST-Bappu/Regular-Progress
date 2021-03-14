list =[23,4,18,52,37,83,49,28,90]
even = [i for i in list if i%2==0] #List Comprehension
print(even)
sqr = [i*i for i in list] #List Comprehension
print(sqr)
num = [1,2,3,4,5,6]
cities=["Dhaka","Chattogram","Khulna","Cumilla","Barishal","Rajshahi"]
z= zip(num,cities) #Zip function
for i in z:
    print(i)
d = {seq:city for seq, city in zip(num,cities)} #Dictionary comprehension
print(d)