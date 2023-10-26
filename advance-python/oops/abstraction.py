"""
Abstraction is one of the four fundamental principles of object-oriented programming (OOP), alongside encapsulation, inheritance, and polymorphism. Abstraction refers to the concept of simplifying complex reality by modeling classes based on real-world objects or processes and exposing only the essential characteristics and behaviors while hiding the unnecessary details.
"""

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class circle(Shape):
    def area(self):
        pi = 3.14
        r = 5
        return pi * r * r
    
class triangle(Shape):
    def area(self):
        base = 5
        height = 2
        return 0.5 * base * height
    
obj = triangle()
# print(dir(obj))
print(obj.area())