x=int(input("Enter the number to find factorial:"))
print("The factorial of ",x,"is")
fact=1
for i in range(x,1,-1):
    fact*=i
print(fact)