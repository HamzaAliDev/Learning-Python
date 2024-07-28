# if else conditions and inputs
# check number is even or odd

num = int(input("Enter an integer: "))

if num % 2 == 0:
    print("Number is even: ", num)
else:
    print("Number is odd: ",num)
    
# input 3 numbers and print the largest number

num1 = int(input("Enter 1st integer: "))
num2 = int(input("Enter 2nd integer: "))
num3 = int(input("Enter 3rd integer: "))

if num1 > num2 and num1 > num3:
    print("Largest number is: ",num1)
elif num2 > num1 and num2 > num3:
    print("Largest number is: ",num2)
else:
    print("Largest number is: ",num3)