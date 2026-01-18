import matplotlib.pyplot as plt
import numpy as np

# plot-customization means changing the appearance of the plot by modifying line styles, marker styles, colors, and other visual aspects to enhance readability and aesthetics.

x = np.array([2023,2024,2025,2026])
y1 = np.array([20,15,30,25])
y2= np.array([30,25,35,20])
y3 = np.array([35,20,40,25])

line_style = dict( linestyle='solid',
                   marker='.',
                   markerfacecolor='red',
                   markeredgecolor='red',
                   markersize=10,
                   linewidth=2 )
# print(line_style)

plt.plot(x,y1,color='green', **line_style)# ** unpacks the dictionary= keyword arguments i.e. linestyle='solid', marker='.', etc.
plt.plot(x,y2,color='blue', **line_style)
plt.plot(x,y3,color='orange', **line_style)

plt.show() 

plt.plot(x,y1,'go--')# 'go--' means green color, circle markers and dashed line
plt.plot(x,y2,'b^:')# 'b^:' means blue color, triangle_up markers and dotted line
plt.plot(x,y3,'rs-.')# 'rs-.' means red color, square markers and dash_dot line
plt.show()
