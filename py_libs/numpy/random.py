import numpy as np 

# random number generation in numpy
# rng = np.random.default_rng(seed=1)# (seed=1) --> 'optional' always produce the same result / copy
rng = np.random.default_rng()
# create a random number generator instance
print(rng.random()) # random float in [0.0, 1.0)
print(rng.integers(low=1, high=10 , size=4))# return a list with len of size given
print(rng.integers(low=1, high=10 , size=(3,2)))# return a 2D list with 3 rows & 2 columns


np.random.seed()
# np.random.seed(seed=1)
print(np.random.uniform(low = -1 , high = 1 , size = 3)) # random float in [0.0, 1.0)
print(np.random.uniform(low = -1 , high = 1 , size = (3,2) ))

# array shuffling
array = np.array([1,2,3,4,5])
rng.shuffle(array)
print(array)

fruits = np.array(['🍎','🍏','🍊','🥥','🍌'])
print(fruits)
fruit = rng.choice(fruits, size =3)
print(fruit)
fruit = rng.choice(fruits, size =(3,2) )
print(fruit)