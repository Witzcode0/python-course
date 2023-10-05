"""
Exception handling in Python refers to the process of managing and responding to unexpected or exceptional events that can occur during the execution of a Python program. These exceptional events, known as exceptions, can include errors, unexpected conditions, or other issues that can disrupt the normal flow of a program.

Python provides a mechanism for handling exceptions using the try, except, else, and finally blocks. Here's how it works:


Exception handling in Python refers to the process of managing and responding to unexpected or exceptional events that can occur during the execution of a Python program. These exceptional events, known as exceptions, can include errors, unexpected conditions, or other issues that can disrupt the normal flow of a program.

Python provides a mechanism for handling exceptions using the try, except, else, and finally blocks. Here's how it works:

1] try block: The code that might raise an exception is placed inside a try block. If an exception occurs within this block, Python will immediately jump to the corresponding except block.

2] except block: This block contains code to handle the exception. You can have multiple except blocks to handle different types of exceptions. Each except block specifies the type of exception it can catch. If the exception raised matches the type specified in an except block, that block's code is executed.

3] else block (optional): This block is executed if no exceptions occur in the try block. It is often used for code that should run when there are no exceptions.

4] finally block (optional): This block, if present, is executed regardless of whether an exception occurred or not. It is often used for cleanup operations, such as closing files or releasing resources.

5] The assert statement in Python is a debugging aid that tests a condition as an expression and triggers an AssertionError exception if the condition is False. It's commonly used during development to ensure that certain conditions or assumptions in your code are met. If the condition is True, nothing happens, and your program continues to run as usual. If the condition is False, an AssertionError is raised, which can help you quickly identify issues in your code.


6] Raise an exception
As a Python developer you can choose to throw an exception if a condition occurs.

To throw (or raise) an exception, use the raise keyword.

"""

x = "hello"
if not type(x) is int:
  raise TypeError("Only integers are allowed")

# x = 4
# assert x == 5, "x should be equal to 5"


# print("hello-1")
# try:
#     a = input("Enter a number A : ")
#     b = input("Enter a number B : ")
#     a = int(a)
#     b = int(b)
# except ZeroDivisionError:
#     print("You can not divide any value with 0")
# # except NameError:
# #     print("Oops! You have not define something")
# # except TypeError:
# #     print("value datatype must be integer")
# # except Exception as e:
# #     print(f"ERROR : {e}")
# else:
#     print(a/b)

# finally:
#     print("I will print anyway")
# print("hello-2")