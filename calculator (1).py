def add(x, y):
    return x + y
   
def subtract(x, y):
    return x - y
    
def multiply(x, y):
    return x * y
    
def divide(x, y):
    return x / y
    
def square(x):
    return x * x
    
def sqr(x):
    return x ** (1/2)
    
def cube(x):
    return x ** 3
    
def cuberoot(x):
    return x ** (1/3)
    
def pow(x, y):
    return x ** float(input("Input power: "))
    
print("""Select operation 
1. Add
2. Subtract
3. Multiply
4. Divide
5. Square
6. Square root
7. Cube
8. Cube root
9. Exponential""")

while True:
    choice = input("ENTER CHOICE (1-9): ")
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
    if choice == '1' :
        print(num1, "+", num2, "=", add(num1, num2))
        
    if choice == '2' :
        print(num1, "-", num2, "=", subtract(num1, num2))
        
    if choice == '3' :
        print(num1, "*", num2, "=", multiply(num1, num2))
        
    if choice == '4' :
        print(num1, "/", num2, "=", divide(num1, num2))
        
    if choice in ("9"):
        num1 = float(input("Enter your number: "))
    if choice == ('9') :
        print("The answer is", pow(num1, input))
        
    if choice in ("5", "6", "7", "8"):
        num1 = float(input("Enter your number: "))
        
    if choice == '5' :
        print(num1, "^", '2', "=", multiply(num1, num1))
        
    if choice == '6':
        print(num1, "^", "1/2", "=", sqr(num1))
        
    if choice == '7' :
        print(num1, "^", '3', "=", cube(num1))
        
    if choice == '8' :
        print(num1, "^", "(1/3)", "=", cuberoot(num1))
    