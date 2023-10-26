"""
Inheritance is a fundamental concept in object-oriented programming (OOP), and Python, being an object-oriented programming language, supports inheritance. Inheritance allows you to create a new class that is a modified version of an existing class. The existing class is referred to as the "base class" or "parent class," and the new class is called the "derived class" or "child class."
"""

# class Parents:
#     property = "car"

# class child(Parents):
#     i_have_a_house = True

# obj = child()
# print(dir(obj))

# types of inheritance
# Single Inheritance
# class A:
#     def a():
#         print("I am from class A")

# class B(A):
#     def b():
#         print("I am from class B")

# obj = B()
# print(dir(obj))

# multilevel inheritance
# class A:
#     def a(self):
#         print("I am from class A")

# class B(A):
#     def b(self):
#         print("I am from class B")

# class C(B):
#     def c(self):
#         print("I am from class C")

# obj = C()
# # print(dir(obj))
# obj.a()
# obj.b()
# obj.c()

# multiple inheritence
# class A:
#     def a(self):
#         print("I am from class A")

# class B:
#     def b(self):
#         print("I am from class B")

# class C(A, B):
#     def c(self):
#         print("I am from class C")

# obj = C()
# # print(dir(obj))
# obj.a()
# obj.b()
# obj.c()

# Hierarchical Inheritance
# class dada:
#     def display_property1():
#         print("Property of dada")

# class papa(dada):
#     def display_property2():
#         print("Property of papa")

# class boy(papa):
#     def display_property3():
#         print("Property of boy")

# class girl(papa):
#     def display_property4():
#         print("Property of girl")


# class motapapa(dada):
#     def display_property():
#         print("Property of motapapa")

# obj = girl()
# print(dir(obj))