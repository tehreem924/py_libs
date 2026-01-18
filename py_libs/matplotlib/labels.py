import matplotlib.pyplot as plt
import numpy as np

# labels for x-axis, y-axis and title
x = np.arange(2023,2027)
y1 = np.array([20,30,35,25])
y2 = np.array([30,25,35,20])
y3 = np.array([35,20,40,25])

plt.title("Yearly Data Overview",fontsize = 20,
                                fontweight = "bold",
                                color = "orange",
                                family = "Arial")

plt.xlabel("Year",fontsize = 20,fontweight = "bold",family = "Arial",color = "blue")
plt.ylabel("Students",fontsize = 20,fontweight = "bold",family = "Arial",color = "blue")
plt.plot(x,y1,'go--', label='Dataset 1')# 'go--' means green color, circle markers and dashed line
plt.plot(x,y2,'b^:', label='Dataset 2')# 'b^:' means blue color, triangle_up markers and dotted line
plt.plot(x,y3,'rs-.', label='Dataset 3')# 'rs--.' means red color, square markers and dash_dot line
plt.legend()# to show the legend on the plot --> legend = 
plt.tick_params(axis='both', colors='red' )# to change the color of ticks on both axes to red
plt.xticks(x)
plt.show() 