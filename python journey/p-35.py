with open ("practice.txt","r") as f:
    data=f.read()
new_data=data.replace("am","is")
print(new_data)