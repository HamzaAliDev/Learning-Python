# list and its method.
students = ['ali','umer','zain','maaz','umair']
nums = [22,23,56,87,34,17]
print(students,nums)

# extend method
output = students.extend(nums)
print("output",output,"students",students)

# concatenation
students = ['ali','umer','zain','maaz','umair']
output = students + nums
print("output",output,"students",students)

# index method
output = students.index("maaz")
print("output ",output,"students",students)

# count method
output = students.count('ali')
print("output ",output,"students",students)

# repitition method
output = ['Hy !'] * 7
print("output",output)

# slice method
output = students[1:3]
print("output ",output,"students",students)

# sort method
students.sort()
print("students",students)

newList = ["Ali","Umer",'Zain','Maaz','Umair','ali','umer','zain','maaz','umair']
newList.sort()
print(newList)
      
newList = [23,56,89,3,56,67]
newList.sort()
print(newList)
      
newList = [23,56,89,3,0.4,2.4,8.9,0.1]
newList.sort()
print(newList)

# reverse method
students.reverse()
print("students",students)

newList = [23,56,89,3,56,67]
newList.reverse()
print(newList)

# nested list
nestedList = ["ali","zain","umer",['naveed','sarwar']]
print(nestedList)
print(nestedList[3][1])
print(nestedList[3][1][3])