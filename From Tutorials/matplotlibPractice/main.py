import matplotlib.pyplot as plt

'''x=[i for i in range(7)]
y=[50,51,52,48,47,45,55]
plt.xlabel("Day")
plt.ylabel("Temperature")
plt.title("Weather")
#plt.plot(x,y, color="green", linewidth=5, linestyle="dashdot")
plt.plot(x,y,"gD--",markersize=10,alpha=1)
plt.show()'''
x=[i for i in range(7)]
max_t=[50,51,52,48,47,45,55]
min_t=[42,43,41,39,38,35,45]
avg_t=[(i+j)/2 for i,j in zip(max_t,min_t)]
print(avg_t)
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.title("Weather")
plt.plot(x,max_t,label="Max")
plt.plot(x,min_t,label="Min")
plt.plot(x,avg_t,label="Average")
plt.legend()
plt.show()