import matplotlib.pyplot as plt
import numpy as np

# bar charts
# Example 1
labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
values = [23, 45, 56, 78, 65, 85, 50, 40]
# compulsory parameters: (x-axis = labels and heights of bars = values)
plt.bar(labels, values, color='skyblue')
# plt.barh(labels, values, color='skyblue')# horizontal bar-chart
plt.title('Bar Chart Example')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()

# Example 2
categories = np.array(['A', 'B', 'C', 'D'])
values1 = np.array([23, 45, 56, 78])    
values2 = np.array([34, 23, 67, 89])
x = np.arange(len(categories))  # the label locations or x coordinates --> x=4 for 4 categories
width = 0.35  # the width of the bars
# ax.bar(x- width/2) = ? center the bars on the x ticks 
# compulsory parameters: x-axis=labels and heights of bars = values
plt.bar(x- width/2 ,values1, width, label='Dataset 1', color='skyblue')
plt.bar(x+ width/2, values2, width, label='Dataset 2', color='salmon')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart Example')
plt.xticks(x, categories)# set custom x-axis tick labels
plt.legend()
plt.show()