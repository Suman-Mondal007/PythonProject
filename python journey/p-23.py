nums=(1,4,9,16,25,36,49,64,81,100)
x=int(input("Enter element to search: "))
i=0
while i < len(nums):
    if(nums[i] == x):
        print("Element found at index ",i)
    i+=1
