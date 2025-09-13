f=open("demo.txt","r")
data=f.read()
print(data)
f.close()


f=open("demo.txt","w")
f.write("i am suman")
f.close()

f=open("demo.txt","a")
f.write(" i love something")  #add next
f.close()

import os
os.remove("demo.txt")
