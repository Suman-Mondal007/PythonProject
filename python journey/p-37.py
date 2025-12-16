# import numpy as np
# arr = np.array([1,2,3,4,5])
# print(arr[0])
# print(arr[-1])
#
#
# #slicing
# print(arr[1:3])
# print(arr[:3])
# print(arr[::2])  #every second element
# print(arr[::-1]) #reverse
#
# #fancy indexing
# print(arr[[0,1,3]])
#
# #boolean masking
# print(arr[arr>3])



#reshaping
import numpy as np
arr = np.array([1,2,3,4,5,6])
x=arr.reshape(3,2)
print(x)

#ravel and flatten
arr2=np.array([[1,2,3],[4,5,6]])
print(arr2.ravel())  #view
print(arr2.flatten())