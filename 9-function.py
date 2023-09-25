"""a function is a reusable block of code that performs a specific task or set of tasks. Functions are essential in programming because they allow you to break down a program into smaller, more manageable pieces, making your code more organized, readable, and maintainable. Functions can accept input data, known as arguments or parameters, and can return output data as a result.

Here's a basic syntax for defining a function in Python:

def function_name(parameters):
    # Function body
    # Perform some operations
    return result  # Optional

    
Let's break down the key components of a Python function:

def: This keyword is used to define a function.

function_name: This is the name of the function, which you choose to represent the task it performs. Function names follow the same naming conventions as variable names.

parameters (optional): These are placeholders for the data that you can pass into the function when you call it. Parameters are enclosed in parentheses and separated by commas. If a function doesn't take any parameters, the parentheses remain empty.

Function body: This is an indented block of code that contains the statements and logic that define what the function does.

return (optional): This keyword is used to specify the value that the function should return as its result. Not all functions have to return a value, and you can omit the return statement if the function is intended to perform some actions without producing a result.

Types of parameters :

Positional Parameters:

These are the most common type of parameters in Python functions.
They are defined in the function's parameter list and are assigned values based on their position when the function is called.
The order in which you provide arguments when calling the function determines which parameter each argument corresponds to.

Example : 
def add(a, b):
    return a + b

result = add(3, 5)  # Here, 3 is assigned to 'a' and 5 is assigned to 'b'


Keyword Parameters:

Also known as named parameters, keyword parameters are explicitly named when calling the function.
They allow you to specify the parameter names along with their values, making it clear which value corresponds to which parameter.
They are helpful for improving code readability, especially in functions with many parameters.

Example :
def divide(dividend, divisor):
    return dividend / divisor

result = divide(dividend=10, divisor=2)  # Explicitly naming parameters


Default Parameters:

Default parameters have default values assigned to them when the function is defined.
If a value is not provided for a default parameter when the function is called, it uses the default value.
Default parameters are useful when you want to make some parameters optional.

Example : 
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

result1 = greet("Alice")       # Uses the default 'greeting' value
result2 = greet("Bob", "Hi")  # Overrides the default 'greeting' value


Variable-Length Parameters:

Python allows you to define functions that can accept a variable number of arguments.
There are two types of variable-length parameters: *args and **kwargs.
*args (Arbitrary Positional Arguments):
Allows you to pass a variable number of positional arguments to a function.
These arguments are received as a tuple within the function.

Example :

def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

result = sum_numbers(1, 2, 3, 4, 5)


**kwargs (Arbitrary Keyword Arguments):
Allows you to pass a variable number of keyword arguments to a function.
These arguments are received as a dictionary within the function.

Example :
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Alice", age=30, city="New York")


Unpacking Parameters:

You can use the * operator to unpack an iterable (e.g., a list or tuple) when calling a function with positional parameters, or ** to unpack a dictionary when calling a function with keyword parameters.

Example :
def add(a, b, c):
    return a + b + c

values = [1, 2, 3]
result = add(*values)  # Unpacking a list


variables can have different scopes, primarily local and global scopes, which determine where in the code a variable can be accessed. 


Local Variables:

Local variables are defined within a specific block or scope, such as within a function.
They are only accessible within the block where they are defined.
Local variables are created when a function is called and destroyed when the function exits.
These variables cannot be accessed outside of the function in which they are defined.

Example : 
def my_function():
    x = 10  # 'x' is a local variable
    print(x)

my_function()
# print(x)  # This would raise an error because 'x' is not defined in this scope

Global Variables:

Global variables are defined at the top level of a Python script or in the global scope.
They are accessible from any part of the code, both inside and outside of functions.
Global variables persist throughout the entire program's execution.
To modify a global variable from within a function, you need to use the global keyword to indicate that you're working with the global variable, not creating a new local variable with the same name.

Example : 
y = 20  # 'y' is a global variable

def my_function():
    global y
    y += 5  # Modifying the global 'y' variable

my_function()
print(y)  # Output: 25


"""

# num1 = 5

# print(num * num)

# num1 = 7

# print(num1 * num1)

# def sameValueMultiply(n1, n2):
#     return n1 * n2

# num1 = int(input("enter a number : ")) 
# print(sameValueMultiply(num1, num1))

# positional para : 
def add(a,b,c,d):
    return a + b + c + d

# print(add(10,20,30)) # TypeError: add() missing 1 required positional argument: 'd'
# print(add(10,20,30, 40)) 


# keyword parameter:
def bill(tomato=20, onion=25):
    print(tomato + onion) # 45

# bill()

# default para :
def bill(tomato=20, onion=25):
    print(tomato + onion)

# bill(tomato=50)

# variable length

# def add(*yoyo):
#     # print(type(yoyo))
#     sum = 0

#     for num in yoyo:
#         sum += num
#     print(sum)

# add(10,20,30,40,50, 60,70,80,90)

def bill(**products):
    # print(type(products))
    total_amount = 0
    for k, v in products.items():
        print(k ,v)
        total_amount += v

    print("Amount: ", total_amount)

# bill(pen=10, book=20, milk=100, drink=25)


# lambda function

demo = lambda x,y,z:x > y 
print(demo(10, 30, 40))

