"""
Encapsulation is one of the fundamental principles of object-oriented programming (OOP), and it refers to the concept of bundling data (attributes) and the methods (functions) that operate on that data into a single unit called a class. This unit provides a way to control the access to the data, ensuring that it is used in a controlled and consistent manner.

In Python, encapsulation is implemented using access modifiers and naming conventions:

Public: By default, all attributes and methods in a class are considered public. This means they can be accessed from outside the class. You can access them directly.

class MyClass:
    def __init__(self):
        self.public_attribute = 42

obj = MyClass()
print(obj.public_attribute)


Example :
class login:
    def __init__(self):
        self.email = input("Enter your email : ")
        self.password = input("Enter a password")

obj = login()

if obj.email == 'brijesh@gmail.com' and obj.password == '12345':
    print("Now you are logged in")
else:
    print("Invalid credentional")


Protected: In Python, protected attributes and methods are indicated by prefixing their names with a single underscore (e.g., _protected_attribute). These elements should not be accessed from outside the class, but Python doesn't enforce this; it's more of a naming convention.

class MyClass:
    def __init__(self):
        self._protected_attribute = 42

obj = MyClass()
print(obj._protected_attribute)  # This is allowed, but it's considered a convention not to access it directly.


Private: Private attributes and methods are indicated by prefixing their names with double underscores (e.g., __private_attribute). These elements should not be accessed from outside the class, and Python performs name mangling to make it more difficult to access them.

class ATM:
    def __init__(self):
        self.__pin = input("Enter a pin: ")

    def displayPIN(self):
        print(self.__pin)

obj = ATM()
# print(obj.__pin)
# obj.displayPIN()

# you can access private attribute using name mangling method
# syntax : _classname__var
print(obj._ATM__pin)
"""


