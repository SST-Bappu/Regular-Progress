basket = {"Mango","Apple","Orrange","Apple","Grape","Orrange"}
print(type(basket))
print(basket)
b = ["Mango","Apple","Orrange","Apple","Grape","Orrange"]
unique_fruits = set(b)
print(type(b),type(unique_fruits))
unique_fruits.add("Pomegranate")
print(unique_fruits)
fs = frozenset(b) #It does the same thing as set does
print(fs)
#fs.add("something")--> Only difference is we can add elements to frozen set
#we can't also change the content of froze set