import numpy as np

# filtering in numpy = selecting elements from an array based on a condition or criteria.  

array = np.array([10,15,20,25,30,35,40,45,50]) 
mask = array > 25
print(f'Boolean mask: {mask}')  # Output: [False False False False  True  True  True  True  True]
 
filtered_array = array[mask]
print(f'Filtered array: {filtered_array}')  # Output: [30 35 40 45 50]

# using np.where to filter elements ,it keeps the original shape of the array ,but its slower than boolean indexing
# np.where( condition , array , replacement_value )
filtered_array_where = np.where(array > 25, array, -1) # elements greater than 25 are kept, others set to -1
print(f'Filtered array using np.where: {filtered_array_where}')  # Output: [-1 -1 -1 -1 30 35 40 45 50]
