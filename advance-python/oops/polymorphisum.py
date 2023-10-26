"""
Polymorphism is one of the fundamental principles of object-oriented programming (OOP), and it refers to the ability of different objects to respond to the same method or message in a way that is specific to their individual types. In other words, polymorphism allows objects of different classes to be treated as objects of a common base class, and their methods can be called without knowing their specific class. Polymorphism promotes code reusability and flexibility.

There are two main types of polymorphism in OOP:

Compile-time (Static) Polymorphism: This is achieved through method overloading and operator overloading. It is resolved at compile time. Method overloading allows multiple methods in the same class with the same name but different parameter lists. The correct method is chosen by the number and type of arguments at compile time. Operator overloading allows you to define how operators behave for user-defined classes.


Run-time (Dynamic) Polymorphism: This is achieved through method overriding. It is resolved at runtime. Method overriding allows a subclass to provide a specific implementation of a method that is already defined in its superclass. The specific method to be executed is determined by the object's actual class at runtime.
"""

# class maths:
#     def add(self, a, b):
#         return a + b
    
#     def add(self, a, b, c):
#         return a + b + c
    
# obj = maths()
# print(dir(obj))
# print(obj.add(10,20, 30))

# x = 10
# x = 20
# print(x)

# class Calculator:
#     def add(self, a, b):
#         return a + b

#     def add(self, a, b, c):
#         return a + b + c

# calc = Calculator()
# result1 = calc.add(2, 3)      # Calls the first add method
# result2 = calc.add(2, 3, 4)   # Calls the second add method

# class Calculator:
#     def add(self, a, b, c=None):
#         if c is not None:
#             return a + b + c
#         else:
#             return a + b

# calc = Calculator()
# result1 = calc.add(2, 3)      # Calls the first add method
# result2 = calc.add(2, 3, 4)   # Calls the second add method

# print(result1)  # Output: 5
# print(result2)  # Output: 9


class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def animal_sound(animal):
    return animal.speak()

dog = Dog()
cat = Cat()

print(animal_sound(dog))  # Output: "Woof!"
print(animal_sound(cat))  # Output: "Meow!"
