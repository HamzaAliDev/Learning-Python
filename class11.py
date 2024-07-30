# map and filter loop

names = ['Ali','Zain','Haris','Zia','Moiz']
def changeName(item):
    return f"Hellow " + item
newList = list(map(changeName,names))
print(newList)

# using anonymous function
newList = list(map(lambda x: f'Hy ' + x, names))
print(newList)

# filter loop
nums = [11,12,13,14,15,16,17,18,19,20]
def selectEven(i):
    if i%2 == 0:
        return i
newList = list(filter(selectEven,nums))
print(newList)

# using anonymous funstion
newList = list(filter(lambda x: x%3 == 0 , nums))