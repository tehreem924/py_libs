import matplotlib.pyplot as plt
import numpy as np

# x = np.array([2023,2024,2025,2026])
x = np.arange(2023,2027)
y = np.array([20,30,35,25])
plt.plot(x,y)
plt.show()
plt.plot(y)# plots y against its index values
plt.show()

plt.plot(x,y,'ro')# 'ro' means red color and circle markers
plt.show()
