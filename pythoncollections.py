#python collections

# List[] Ordered, changeable, allows duplicates(insert(),append(),extend(),pop())
a = [1,2,3,4,5,6]
b = [7,8,1]
a.append(7)
a.insert(1,8)
a.pop()
a.pop(1)
b.extend(a)
print(b)
print(a)
print(a[2])
# Tuple()  allow duplicate, any type of data can store we cannot modify 
x = (1,2,3,4,5,6)
y=list(x) # We are changed tuple to list
y.append([2])
y.pop()
print(y)
# Set{} Do not allow Duplicate values will r removed, any type data can restored,we cannot modify and unordered(add(),update(),remove(),pop())
m = {1,2,3,7,4,5,6}
m.pop()
m.add(9)
m.update([10,8])
m.remove(5)
print(m)
# Dictionary{} Do not allow Duplicate,Duplicate value will overwrite existing values. any data can store Key:Value pair {"name":"Mani"}
n= {
     "Name": "Mani",
     "Age" : 36,
     "mark": 350,
     "DOB" : 2003,
     }
n["Age"]=21
print(n.keys())
print(n.values())
print(n["Name"])


