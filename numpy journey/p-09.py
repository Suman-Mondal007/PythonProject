import numpy as np
prices=[100,200,300]
discount=10
final_prices=[]
for price in prices:
    final_price=price-(price*discount/100)
    final_prices.append(final_price)
print(final_prices)


#using broadcasting
prices=np.array([100,200,300])
discount=10
final_prices=prices-(prices*discount/100)
print(final_prices)


arr1=np.array([[1,2,3],[4,5,6]])
arr2=np.array([[1,2,3]])    #if not same order then give error
result=arr1+arr2
print(result)


#vectorization
arr1=np.array([[1,2,3]])
arr2=np.array([[4,5,6]])    #if not same order then give error
result=arr1+arr2
print(result)