info={
    "name":"suman",
    "Age" : 22,
    "marks": 8.9,
    "roll":166,
    "Dept":"cse"
}
print(info)
print(info["name"])
print(info["Age"])


info["surname"]="mondal"
print(info)


#nested dictionary
student={
    "name":"suman",
    "Age": 22,
    "marks":{
    "ben":86,
    "eng":95,
    "math":88,
    }
}
print(student)
print(student["marks"])
print(student["marks"]["ben"])
print(list(student.keys()))
print(len(student))

new_dict={"class":"sec-c"}
student.update(new_dict)
print(student)

