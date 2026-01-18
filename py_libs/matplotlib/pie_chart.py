import matplotlib.pyplot as plt
import numpy as np

#  pie-chart

# Example 1
labels = np.array(['A', 'B', 'C', 'D'])
sizes = np.array([15, 30, 45, 10])
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)# autopct --> display percentage value on each slice 
plt.title('Simple Pie Chart')
plt.show()

# Example 2
labels = np.array(['A', 'B', 'C', 'D'])
sizes = np.array([25, 35, 25, 15])
colors = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen']
explode = (0.1, 0, 0, 0)  # explode 1st slice
plt.pie(sizes, labels=labels, colors=colors, explode=explode,
        autopct='%1.1f%%', shadow=True, startangle=140)# startangle --> rotate the start of the pie chart
plt.title('Exploded Pie Chart with Custom Colors')
plt.show()

# Example 3
labels = np.array(['A', 'B', 'C', 'D', 'E'])
sizes = np.array([20, 25, 30, 15, 10])
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99', '#c2c2f0']
explode = (0.05, 0.05, 0.05, 0.05, 0.05)  # explode all slices slightly
plt.pie(sizes, labels=labels, colors=colors, explode=explode,
        autopct='%1.1f%%', shadow=True, startangle=90, wedgeprops={'edgecolor': 'black'})# wedgeprops --> customize slice properties
plt.title('Customized Pie Chart')
plt.show()
