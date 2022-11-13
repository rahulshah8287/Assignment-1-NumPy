import numpy as np

# 1. Create a null vector of size 10 but the fifth value which is 1
vector = np.zeros(shape=10)
vector[4] = 1
print(vector)

# 2. Create a vector with values ranging from 10 to 49.
vector_1 = np.arange(10,49)
print(vector_1)

# 3. Create a 3x3 matrix with values ranging from 0 to 8
vector_2 = np.arange(0,9)
vector_3 =vector_2.reshape(3,3)
print(vector_3)


# 4. Find indices of non-zero elements from [1,2,0,0,4,0]
list = [1,2,0,0,4,0]
array_1 = np.array(list)
print(array_1)
print(np.nonzero(array_1))


# 5. Create a 10x10 array with random values and find the minimum and maximum values.
array_2 = np.random.randint(low=0, high=100, size=(10,10))
print(array_2.min(), array_2.max())


# 6. Create a random vector of size 30 and find the mean value.
array_3 = np.random.randint(low=0, high=100, size=30)
print(array_3.mean())