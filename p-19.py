collections={1,2,3,3,3,5,3,8,9}
print(collections)  #ignore duplicate value

collections=set()# empty set
collections.add(1)
collections.add(2)
collections.add(3)
print(collections)
collections.remove(3)
print(collections)
collections.clear()
print(collections)

set1={1,2,3,4}
set2={3,4,5,6}
print(set1.union(set2))  #union
print(set1.intersection(set2)) #intersection
print(set1)