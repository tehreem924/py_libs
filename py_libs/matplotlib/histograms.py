import matplotlib.pyplot as plt
import numpy as np

# histogram data is usually used to represent the distribution of numerical data by dividing the entire range of values into a series of intervals (bins) and counting how many values fall into each interval.

# Example 1
data = np.random.randn(1000)# randn --> normal distribution and here it gives 1000 random numbers
plt.hist(data, bins=20, color='blue', edgecolor='black', alpha=0.7)
plt.title('Histogram Example')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# Example 2
data1 = np.random.normal(60, 10, 1000)  # mean=80, std=1
data2 = np.random.normal(60, 10, 1000)  # mean=70, std=5
plt.hist([data1, data2], bins=20, color=['blue', 'orange'], edgecolor='black', alpha=0.7, label=['Dataset 1', 'Dataset 2'])
plt.title('Overlapping Histograms') 
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()
plt.show()
