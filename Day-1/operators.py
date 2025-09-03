def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
def moduloDiv(x,y):
    return x%y
x,y=map(int,input("Enter the x and y values:").split(","))
print("Addition of x and y ",add(x,y))
print("Subtraction of x and y ",subtract(x,y))
print("Multiplication of x and y ",multiply(x,y))
print("Division of x and y ",divide(x,y))
print("Modulo Division of x and y ",moduloDiv(x,y))