import numpy as np

# Create a 10x10 matrix with random values between 0 and 100
matrix = np.random.randint(0,100 ,size=(10, 10))

# Display the matrix
print("10x10 Random Matrix:\n", matrix)

# Find minimum value
min_value = np.min(matrix)

# Find maximum value
max_value = np.max(matrix)

# Display results
print("\nMinimum Value:", min_value)
print("Maximum Value:", max_value)


a=np.random.rand(2,2)
print(a)

b=np.eye(3,3)
print(b)