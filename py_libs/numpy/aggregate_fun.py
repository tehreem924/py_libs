import numpy as np

# Aggregate functions in NumPy = functions that operate on an array and return a single value or a reduced array.

arr = np.array([[1,2,3,4,5],
                [6,7,8,9,10]])

print(np.sum(arr))
print(np.mean(arr))
print(np.std(arr))# standard deviation
print(np.var(arr))# variance
print(np.min(arr))
print(np.max(arr))
print(np.argmin(arr))# return index of the minimum value
print(np.argmax(arr))
print(np.sum(arr, axis=0)) # sum of each column
print(np.sum(arr, axis=1)) # sum of each row
print(np.cumsum(arr)) # cumulative sum of elements 
print(np.cumprod(arr)) # cumulative product of elements or factorial
