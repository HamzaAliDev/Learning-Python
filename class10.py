# for loop.
num = [11,12,13,14,15,16,17,18,19,20]

for item in num:
    print(item)
    
for item in range(0,20,2):
    print(item)
    
 
# write a program to search ali from a list, if ali found then loop terminate and print ali   
std = ["zain","moiz","ali","haris","taha","bilal"]
search = False
for item in std:
    if item == "ali":
        search = True
        break
    
if search:
    print("Search is found: ",item)
else:
    print("Search is not found")
    
