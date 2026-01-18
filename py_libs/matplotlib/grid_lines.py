import matplotlib.pyplot as plt 

# grid() function helps make plot easier to read by adding grid lines
x = [1,2,3,4,5]
y = [10,15,20,25,30]

plt.plot(x,y)
plt.grid(axis='both', color='lightgray', linestyle='--', linewidth=2)
plt.show()