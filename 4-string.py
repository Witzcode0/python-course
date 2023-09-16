"""
a string is a sequence of characters enclosed within either single quotes (') or double quotes ("). Strings are one of the fundamental data types in Python and are used to represent text or character data.

Here are some key characteristics and features of strings in Python:

- Immutable: Strings in Python are immutable, which means their content cannot be changed once they are created. If you need to modify a string, you must create a new string with the desired modifications.

- Sequence of Characters: A string is essentially a sequence (or collection) of characters. Each character in a string has a specific position, known as an index. Indexing in Python starts from 0 for the first character.

- Concatenation: You can concatenate (combine) two or more strings using the + operator. For example, "Hello, " + "world!" results in the string "Hello, world!".

- Escape Sequences: Strings can contain escape sequences, which are special characters preceded by a backslash (\) that have specific meanings. For example, "\n" represents a newline character, and "\t" represents a tab character.

- Multiline Strings: Python allows you to create multiline strings using triple quotes (''' or \"\"\"). This is useful for representing multiline text or code blocks.

- String Methods: Python provides a rich set of string methods that allow you to manipulate and work with strings. Some common methods include split(), strip(), upper(), lower(), replace(), and join(), among others.

- String Indexing and Slicing: You can access individual characters of a string using indexing and extract substrings using slicing.

- Length: Determining the number of characters in a string, usually done with a built-in function like len().

- Substring: Extracting a portion of a string, which can be achieved by specifying a range of indices.

- Search and Replace: Finding specific substrings within a string and replacing them with other substrings.

- Comparison: Comparing two strings to check if they are equal or if one comes before the other in lexicographic order.

- Case Conversion: Changing the case of characters within a string, such as converting all characters to uppercase or lowercase.


syntax :  str_name = ''/""
For example: 

name = "Python"

Indexing : 
    positive_index  Negetive_index
    (left to right) (right to left)  
P   0               -6
y   1               -5
t   2               -4
h   3               -3
o   4               -2
n   5               -1


Slicing :

slicing refers to the operation of extracting a portion of a sequence, such as a string, list, or tuple, by specifying a range of indices. Slicing allows you to create a new sequence that contains a subset of the elements from the original sequence. The basic syntax for slicing in Python is as follows:

syntax : sequence[start:stop:step]

# formatting a sting :
you can format strings using various techniques and methods. Here are some common ways to format strings:
- String Concatenation: You can concatenate (join together) strings using the + operator. 

- String Interpolation (f-strings, available in Python 3.6 and later): F-strings are a convenient way to format strings by embedding expressions inside string literals using curly braces {}.

- .format() Method: The .format() method is another way to format strings, where you can define placeholders within the string and later replace them with values. 

- % Operator (legacy formatting):Python also supports the % operator for string formatting. This method is less recommended for new code and has been largely replaced by f-strings and .format(). 

"""

name = "Python code"

# accessing element of string

# indexing (+)
print(name[4]) # o

# indexing (-)
print(name[-4]) # c

# slicing (+)
print(name[::])
print(name[2:6:]) # thon
# slicing (-)
print(name[-4::]) # code

# concat
fname = "brijesh"
lname = "gondaliya"
print(fname + " " + lname)

# replica
code = "python"
print(code * 3)

# methods
company_name = "MolMEH TecHNOlaB"

print(company_name.swapcase()) # mOLmeh tEChnoLAb

# print(company_name.count("M")) # 2
# # print(dir(company_name))
# print(company_name.capitalize())
# print(company_name.title())
# print(company_name.lower())
# print(company_name.upper())

# password = "Test@123456"
# digit = "12344"
# alpha = "sjkhkbg"
# special_char = "@#$%^&*()"

# print(company_name.isalnum()) # False
# print(company_name.isdigit()) # False
# print(company_name.isalpha()) # False
# print(digit.isdigit()) # True
# print(alpha.isalpha()) # True
# print(special_char.isalnum()) # False
# print(not special_char.isalnum()) # True


# name = "     brijesh     "

# print(len(name)) # 17
# print(name.lstrip())
# print(name.rstrip())
# print(name.strip())

name = "test"
print(name.center(20, '-'))

# formated string

name = "brijesh"
age = 27

print("Your name is " + name + " and your age is " + str(age))
print(f"Your name is {name} and your age is {str(age)}")
print("Your name is {} and your age is {}".format(name, str(age)))
print("Your name is {1} and your age is {0}".format(name, str(age)))

book = "c programming"
price = 345.65376326437

print("Book name : %s and price : %.3f" % (book, price) )