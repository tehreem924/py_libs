import numpy as np

array = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9],
                  [10,11,12] ])

# slicing array(start,end,step)
print(array[0:4:2])
print(array[::2])
# slicing rows and columns
print(array[:,1:3])
# slicing specific rows and columns (0 to 2 rows and 0 to 2 columns)
print(array[1:3,0:2])
#slicing with negative step (reversing the array)
print(array[::-1,::-1])
# slicing all rows and reversing row order
print(array[::-1,:])
#slicing all columns and reversing column order
print(array[:,::-1])
# slicing specific rows and all columns
print(array[1:3,:])
#slicing specific columns and all rows
print(array[:,1:3])
#slicing specific rows and specific columns with step
print(array[0:4:2,0:3:2])
#slicing specific rows and specific columns with negative step
print(array[::-2,::-2])