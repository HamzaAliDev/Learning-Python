# functions in python.
def show():
    print("Hellow World")


def add(a,b):
    num1 = a
    num2 = b
    result = num1 + num2
    print(result)

def sum(a,b):
    c = a + b
    return c
    

show();
add(20,45);
add(sum(10,20),30)

result = sum(10,20) + 10
print(result)

#  build-in function local
print(locals())
