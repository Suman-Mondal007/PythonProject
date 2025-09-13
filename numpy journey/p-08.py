#inserting any value
import numpy as np
arr=np.array([1,2,3,4,5,6,7])
print(arr)
new_arr=np.insert(arr,2,100)
print(new_arr)

"""
for 2d array
axis=0 for row wise add
axis=1 for col wise add
"""
arr=np.array([[1,2],[3,4]])
print(arr)
new_arr=np.insert(arr,1,[5,6],axis=0)
print(new_arr)


#append
arr =np.array([1,2,3,4,5,6,7])
new_arr=np.append(arr,[8,9])
print(new_arr)


#add two array
arr =np.array([1,2,3])
arr2=np.array([4,5,6])
new_arr=np.concatenate((arr,arr2))
print(new_arr)


#delete
arr =np.array([1,2,3,4,5,6,7])
new_arr=np.delete(arr,2)  #(arr,index)
print(new_arr)

#for 2d array
arr =np.array([[1,2,3],[4,5,6]])
new_arr=np.delete(arr,0,axis=0)
print(new_arr)


