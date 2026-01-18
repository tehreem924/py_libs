import matplotlib.pyplot as plt
import numpy as np

# scatter-plots = points plotted on horizontal and vertical axis to show relationship between two variables

# Example 1 
x1 = np.array([5 ,7 ,8 ,7 ,12 ,8 , 11 ,9 , 4,6,7,9 ,6])
y1 = np.array([99,86,87,88,100,86,103,87,94,78,77,85,86])
x2 = np.array([4,6,7,8,5,7,9,6,5,8,7,9,4])
y2 = np.array([70,78,75,80,72,78,75,73,68,74,77,79,72])
# compulsory parameters: x-axis values and y-axis values
plt.scatter(x1, y1, color='blue', marker='o', label='Class A',alpha=0.5, s=50)# 'o' means circle marker,s-->size, alpha = transparency level (0=transparent, 1=opaque)
plt.scatter(x2, y2, color='red', marker='s', label='Class B',alpha=0.5, s=50)# 's' means square marker
plt.title('Test Scores vs Hours Studied')   
plt.xlabel('Hours Studied')
plt.ylabel('Test Score')
plt.legend()# to show the legend on the plot 
plt.show()
