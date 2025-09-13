def calculator(n):
    if n==0:
        return 0
    return calculator(n-1)+n
x=int(input("Enter a number:"))
print("sum is:",calculator(x))