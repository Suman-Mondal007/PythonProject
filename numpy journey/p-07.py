#reshaping
import numpy as np
arr = np.array([1,2,3,4,5,6])
x=arr.reshape(3,2)
print(x)

#ravel and flatten
arr2=np.array([[1,2,3],[4,5,6]])
print(arr2.ravel())  #view
print(arr2.flatten())   #copy
