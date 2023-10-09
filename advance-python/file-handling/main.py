"""
File handling in Python is a crucial aspect of working with data and storing information persistently. Python provides built-in functions and libraries to interact with files on your computer.

1] Opening and Closing Files:
To work with files, you first need to open them using the open() function and later close them using the close() method.


Syntax : 
file = open("filename.txt", "mode")
# Your file operations here
file.close()

2] Writing to Files:
You can write data to a file using the following methods:
write(): Writes a string to the file.
writelines(): Writes a list of strings to the file.


3]Reading from Files:
You can read the contents of a file using the following methods:

read(): Reads the entire file as a string.
readline(): Reads one line at a time.
readlines(): Reads all lines into a list.

4] Appending to Files:
You can append data to an existing file using the "a" mode.


5] Checking File Existence:
You can use the os.path.exists() function to check if a file exists before attempting to open or manipulate it.

"""

import os

# create a file
# file = open("example.txt", "x") 

# write data into a file
# file = open("example.txt", "w") 
# # file.write("This is a python programming language")
# lines = ['this is a line - 1\n', 'this is a line - 2\n', 'this is a line - 3\n', 'this is a line - 4\n', 'this is a line - 5\n']
# file.writelines(lines)
# file.close()


# read data from the file
# file = open('example.txt', "r")

# print(file.read())
# print(file.read(6))
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readlines())

# file.close()

# print(file.read()) # ValueError: I/O operation on closed file.


# append data into a file
# with open("example.txt", "a") as file:
#     file.write("New log entry\n")


# Checking File Existence:
# if os.path.exists("example.txt"):
#     print("File is exist.")
# else:
#     print("File does not exist.")