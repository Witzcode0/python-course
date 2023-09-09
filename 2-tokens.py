"""
Identifiers
    - Identifiers are used to name variables, functions, classes, modules, and other objects. Python has several rules and conventions for naming identifiers:

Rules of identifiers :
1] Valid Characters:
Identifiers can consist of letters (uppercase or lowercase), digits, and underscores (_).
They must start with a letter (a-z, A-Z) or an underscore (_). They cannot start with a digit (0-9).

2] Case Sensitivity:
Python is case-sensitive. This means that uppercase and lowercase letters are treated as distinct characters. For example, myVar and myvar are considered different identifiers.

3] Reserved Words:
You cannot use Python's reserved words (keywords) as identifiers. Examples of reserved words include if, else, while, for, class, def, and so on.

4]Length:
There is no strict limit on the length of an identifier, but it's recommended to keep them reasonably short and meaningful.

5]Underscores:
It is common to use underscores to separate words in longer identifiers, following the convention known as "snake_case." For example, my_variable, user_name, or calculate_average.

6]CamelCase:
For class names, it is common to use CamelCase, also known as "CapitalizedWords." In this convention, each word within the identifier starts with a capital letter, and there are no underscores. For example, MyClass, EmployeeRecord.

7]Leading Underscore:
By convention, an identifier starting with a single underscore (_) is considered "private" and should not be accessed from outside the module where it is defined. For example, _private_var or _private_function.

8] Double Underscores:
Identifiers that start and end with double underscores (e.g., __init__) have a special meaning in Python. They are often used for name mangling to avoid naming conflicts in subclasses.

Valid Identifiers:
variable_name
my_var
myVar
PI
calculate_average
MyClass
__init__
_private_var

Invalid Identifiers (due to various reasons):
3invalid_var    # Starts with a digit
if             # Reserved keyword
for-loop       # Contains a hyphen (-)
my.variable    # Contains a dot (.)





Variables
What is variable?
A variable is a symbolic name that represents or refers to a value stored in the computer's memory. Variables are used to store and manipulate data within a program. Unlike some programming languages, Python is dynamically typed, which means that you don't need to declare the data type of a variable explicitly. Python infers the data type based on the value assigned to the variable.

Variable Declaration: 
You can declare a variable by assigning a value to it using the assignment operator (=). 
>>> variable_name = value

Example:
my_variable = 42 # int
name = "John" # str
is_valid = True # bool
price = 34.7 $ float
complexNum = 34 + 76j


Variable Naming Rules: 
Variable names in Python must adhere to the following rules:

- They must start with a letter (a-z, A-Z) or an underscore (_).
- The remaining characters can include letters, digits (0-9), and underscores (_).
- Variable names are case-sensitive, so my_var and My_Var are different variables.
- Variable names should be descriptive and follow naming conventions like snake_case (e.g., my_variable, user_name) for better code readability.

Dynamic Typing: Python is dynamically typed, which means you can change the type of a variable by assigning a different value to it. 
my_variable = 42     # Now my_variable is an integer
my_variable = "Hello"  # Now my_variable is a string

Scope: Variables can have different scopes in Python, such as local scope (inside a function), enclosing scope (if defined within a nested function), and global scope (defined outside of functions). The scope determines where the variable is accessible and how it behaves.

Deleting Variables: You can delete a variable using the del statement:
my_variable = 42
del my_variable  # Deletes the variable




Keywords
keywords are reserved words that have special meanings and serve as fundamental building blocks of the language's syntax. 

These keywords cannot be used as identifiers (variable names, function names, class names, etc.) because they are already predefined and used by the Python language itself to perform specific tasks or operations.

Keywords are an integral part of Python's grammar and are used to define the structure and behavior of Python programs.

Step - 1] Go to IDEL or CMD 
Step - 2] Make sure you are in a intractive mode
Step - 3] Write help() and hit on enter
>>> help()

Welcome to Python 3.11's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the internet at https://docs.python.org/3.11/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help>

Step - 4 : Write keywords and hit on enter
help> keywords

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not


1] Control Flow Keywords:
if, elif, else: Used for conditional branching.
for, while: Used for loop constructs.
break, continue: Used for controlling loops.
return: Used to return values from functions.
try, except, finally: Used for exception handling.
pass: Used as a placeholder for empty blocks or functions.

2] Boolean Keywords:
True, False: Used to represent boolean values.

3] Logical Keywords:
and, or, not: Used for logical operations (and, or, not).

4] Function and Class Keywords:
def: Used to define functions.
class: Used to define classes.

5] Import and Module Keywords:
import: Used to import modules.
from: Used in combination with import to import specific objects from modules.
as: Used for aliasing when importing or renaming variables.

6] Variable and Data Type Keywords:
None: Represents a null or uninitialized value.
global, nonlocal: Used to work with variable scopes.

7] Concurrency Keywords (Python 3.5 and later):
async, await: Used for asynchronous programming.

8] Assertion Keywords:
assert: Used for debugging and testing by asserting a condition.

9] Other Keywords:
del: Used to delete references to objects.
lambda: Used to create anonymous (unnamed) functions.




Datatypes
data types are used to categorize and manage different types of data that can be stored and manipulated in a program. Python is a dynamically-typed language, which means you don't need to explicitly declare the data type of a variable; the interpreter infers it based on the value assigned to the variable. Python provides a wide range of built-in data types to represent various kinds of data. Here are some of the most commonly used data types in Python:

                                        Datatypes
                                           |
                          |---------|--------|------|-------|
                        Numeric Dictionery Boolean Set Sequence-type
                         |                               |
                    |----|------|                  |-----|----|
                    Int Float Complax            String List Tuple



"""
# Example : 
x = 10
print(type(x)) # <class 'int'>

y = 45.6
print(type(y)) # <class 'float'>

a = 34 + 78j
print(type(a)) # <class 'complex'>

b = True
print(type(b)) # <class 'bool'>

z = 'python code'
print(type(z)) # <class 'str'>

c = list()
c = []
print(type(c)) # <class 'list'>

d = tuple()
d = ()
print(type(d)) # <class 'tuple'>

e = set()
e = {1,2,4,5}
print(type(e)) # <class 'set'>

f = dict()
f = {
    'key1':'value1',
    'key2':'value2',
}
print(type(f)) # <class 'dict'>

"""
the isinstance() function is used to check the data type of an object. It allows you to determine if an object is an instance of a particular class or if it is a subclass of that class. Here's the basic syntax of the isinstance() function:

isinstance(object, classinfo)

object: The object you want to check the type of.
classinfo: A class, a type, or a tuple of classes and types to check against.

"""

# Check if a variable is an integer
x = 42
if isinstance(x, int):
    print("x is an integer")

# Check if a variable is a string or a float
# y = "Hello, World!"
y = 3.5
if isinstance(y, (str, float)):
    print("y is either a string or a float")

# Check if an object is an instance of a specific class
class Dog:
    pass

dog_instance = Dog()
if isinstance(dog_instance, Dog):
    print("dog_instance is an instance of the Dog class")

"""
In the first example, isinstance(x, int) checks if the variable x is an integer. In the second example, isinstance(y, (str, float)) checks if the variable y is either a string or a float. In the third example, isinstance(dog_instance, Dog) checks if dog_instance is an instance of the Dog class.
"""
