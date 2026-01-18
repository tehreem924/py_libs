import numpy as np

#Basic arithmatic operations
#Scalar operations
a = np.array([1,2,3])
print(f'{a-1}\n{a+2}\n{a*3}\n{a/2}\n{a**3}')

#vectorized operations
a = np.array([1,2,3])
b = np.array([1.23 , 2.31 , 3.05])
print(f'{a * np.pi}\nRadius : {np.round(np.pi * a**2 ,2)}\n{np.ceil(b)}\n{np.floor(b)}\n{np.sqrt(a)}')


#Element-wise arithmatic
a = np.array([1,2,3])
b = np.array([4,5,6])
print(f'{a+b}\n{a-b}\n{a*b}\n{a/b}\n{a**b}') 

#Comaprison operators
a = np.array([56,90,78,80,100,92,68])
print(a >=60)
a[a<60] = 0
print(a)