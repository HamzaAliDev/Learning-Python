# while Loop.
i = 1
while i<=10:
    print("Hellow",i)
    i +=1

# program input a list of number and print the element of list with multiply with 2
userList = []
updatedList = []
print("Enter 5 integers for List")
i = 1
while i <=5:
    userList.append(int(input("Enter integer: ")))
    i += 1
print(userList)

i = 0
while i < 5:
    updatedList.append(userList[i] * 2)
    i += 1
    
print("updatedList",updatedList)