import numpy as np

# Broadcasting in NumPy
# Broadcasting allows NumPy to perform operations on arrays of different shapes in a way that
#  makes sense mathematically or by virtually expanding their dimensions.
# The smaller array is "broadcast" across the larger array so that they have compatible shapes. 
# Two dimensions are compatible when:
# 1. They are equal \ have same size, or
# 2. One of them is 1           (1,4) and (4,1) are compatible 
# If the dimensions are not compatible, NumPy raises a ValueError. 


# Example 1: Adding a scalar to an array
array_1d = np.array([1, 2, 3])
scalar = 5
result_1 = array_1d + scalar
print(f'Example 1 - Adding a scalar to an array: {result_1}') # Output: [6 7 8]

# Example 2: Adding two arrays of different shapes
arr1 = np.array([[1,2,3,4]])
arr2 = np.array([[1],[2],[3],[4]])
print(arr1.shape)  # shape (1 , 4)
print(arr2.shape)  # shape (4 , 1) 
print(arr1 * arr2) # shape (4 , 4) 
# arr1 is broadcasted to shape (4, 4) by repeating its row, and arr2 is broadcasted to shape (4, 4) by repeating its column.
 

arr1 = np.array([[1,2,3,4,5,6,7,8,9,10]])
arr2 = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
print(arr1.shape)  # shape (1 , 10)
print(arr2.shape)  # shape (10 , 1) 
print(arr1 * arr2) # shape (10 , 10) 


# Example 3: Broadcasting with higher-dimensional arrays
array_3d = np.array([[[1]], [[2]], [[3]]])  # Shape (3, 1, 1)
array_2d = np.array([[10, 20, 30, 40]])  # Shape (1, 4) 
result_3 = array_3d + array_2d  # Broadcasting to shape (3, 4)      
print(f'Example 3 - Broadcasting with higher-dimensional arrays:\n{result_3}')

