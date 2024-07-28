# list and its method.
students = ['ali','zain','umer','maaz','ayan']
print(students)

# for last index of list
print(students[-1])

# length of list.
length = len(students)
print(length)

# append method
students.append("haider")
print("students = ",students)

# pop method
output = students.pop()
print("Deleted item = ",output," .students = ",students)

output = students.pop(3)
print("Deleted item = ",output," .students = ",students)

# insert method
students.insert(1,"salaar")
print("students = ",students)

# remove method
output = students.remove("salaar")
print("students = ",students)

# copy method
output = students.copy()
print(output,"students = ",students)

# clear method
students.clear()
print("students =",students)