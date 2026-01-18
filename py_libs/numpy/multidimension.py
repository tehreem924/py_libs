import numpy as np

# 0D
array = np.array('A')
print(array.ndim, array.shape)

# 1D
array = np.array(['A','B','C'])
# shape is (3,) meaning 3 elements in one dimension, ndim is 1 meaning one dimension
print(array.ndim, array.shape, array[1])

# 2D 
array = np.array([['A','B','C'],['D','E','F'],['G','H','I']])
# ndim is 2, shape is (3,3) meaning 3 rows and 3 columns, accessing element at row 2, column 1
print(array.ndim, array.shape, array[2,1])
word = array[0,1]+ array[2,2] + array[2,0]
print(word)

# 3D
array = np.array([[[4 , 5 , 6],[7 ,8, 9],[10,11,12]],
                  [[13,14,15],[16,17,18],[19,20,21]],
                  [[22,23,24],[25,26,27],[28,29,30]] 
                  ])
# shape is (3,3,3) meaning 3 depth layers, each with 3 rows and 3 columns, ndim is 3
print(array.ndim,array.shape) 
# multidimentional indexing 
# (depth, row, column)
print(array[2,1,2])