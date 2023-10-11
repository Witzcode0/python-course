"""
In Python, a class is a blueprint or template for creating objects (instances). It defines the structure and behavior of objects that belong to a particular class. A class serves as a blueprint because it encapsulates data (attributes) and functions (methods) that are associated with the objects created from it.

syntax : 
class class_name:
    # data (attributes)
    variable_name = value

    # functions (methods)
    def function_name(paras):
        # block of code

syntax of object
object_name = class_name()

"""

# class shape:
#     name = "square"

#     def area(yoyo):
#         print("area")
    
# obj = shape()
# # print(dir(obj))
# print(obj.name)
# obj.area()


# class registration:
#     # constructor
#     def __init__(self, username, email, password):
#         print("I am auto call")
#         self.u = username
#         self.e = email
#         self.p = password

#     def user_information(self):
#         print(f"information of {self.u}")
#         print("Email : ", self.e)
#         print("Password : ", self.p)

# while (1):
#     user_name = input("Enter your username : ")
#     email = input("Enter your email : ")
#     password = input("Enter your password : ")
#     obj = registration(user_name, email, password)
#     obj.user_information()

 
class car:
    def __init__(self, name, model, color):
        self.n = name
        self.m = model
        self.c = color


    def display(self):
        print(self.c)
        print(self.n)
        print(self.m)

car1 = car("BMW", "XYZ", "red")
# print(car1)
# print(dir(car1))
print(car1.n)
print(car1.m)
print(car1.c)
car1.display()

car2 = car("honda", "abc", "blue")
# print(car2)
# print(dir(car2))
print(car2.n)
print(car2.m)
print(car2.c)
car2.display()