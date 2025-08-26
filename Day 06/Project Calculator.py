print("Welcome to the calculator app")
#Declare variable and accept user input
a = int(input("Please enter the first number: "))
b = int(input("Please enter the second number: "))
operation = input("What operation do you want to perform? - + * /: ")

#create function to add, multiply, subtract and divide the numbers

#addition
def addition(a, b):
    return a + b

#subtraction
def subtraction(a,b):
    return a - b

#multiply
def multiply(a,b):
    return a * b

#divide
def division(a,b):
    if b != 0:
        return a / b
    else:
        print("Error Zero divion")


#perform operation 
def calculator():
    if operation == "+":
        print("Result:", addition(a,b))
    elif operation == "-":
        print("Result:", subtraction(a, b))
    elif operation == "*":
        print("Result:", multiply(a, b))
    elif operation == "/":
        print("Result:", division(a, b))
    else:
        print("Invalid operator.")


calculator()