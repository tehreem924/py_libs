import matplotlib.pyplot as plt
import numpy as np

# subplots() function is used to create multiple plots in a single figure.
# It returns a figure object and an array of Axes objects which can be used to customize each subplot individually.

# Example 1: Creating a 2x2 grid of subplots
fig, axs = plt.subplots(2, 2)
x = np.linspace(start=0, stop= 10, num=100)# num=number of samples , linspace  --> returns evenly spaced numbers over a specified interval
axs[0, 0].plot(x, np.sin(x))
axs[0, 0].set_title('Sine Wave')    
axs[0, 1].plot(x, np.cos(x), 'tab:orange')
axs[0, 1].set_title('Cosine Wave')
axs[1, 0].plot(x, np.tan(x), 'tab:green')
axs[1, 0].set_title('Tangent Wave')
axs[1, 1].plot(x, np.exp(-x), 'tab:red')
axs[1, 1].set_title('Exponential Decay')
plt.tight_layout()# to prevent overlapping of subplots
plt.show()

# Example 2: Creating a 1x3 grid of subplots
fig, axs = plt.subplots(1, 3, figsize=(12, 4))# figsize(width, height)
x = np.array([1,2,3,4,5.6])
axs[0].plot(x, x**2, 'r-')
axs[0].set_title('y = x^2')
axs[1].bar(x, x**3, color='green')# plotting as bar chart
axs[1].set_title('y = x^3')
axs[2].plot(x, np.sqrt(x), 'b-')
axs[2].set_title('y = sqrt(x)')
plt.tight_layout()
plt.show()