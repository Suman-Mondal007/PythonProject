def fact_calculator(a):
    fact=1
    for i in range(a,1,-1):
        fact*=i
    print(fact)

x=int(input("Enter a number:"))
fact_calculator(x)