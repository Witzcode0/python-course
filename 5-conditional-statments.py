"""
Conditional statements in Python are used to make decisions in your code based on certain conditions. They allow you to execute different blocks of code depending on whether a specified condition is True or False. The primary conditional statements in Python are:

if statement: The if statement is used to execute a block of code if a specified condition is True.

syntax : 
if condition:
    # Code to execute if condition is True

Example :
x = 10
if x > 5:
    print("x is greater than 5")

Example :
score = int(input("Enter your score : "))
if score >= 35:
    print("You are pass")

Example :
age = 18
if age >= 18:
    print("You are eligible to vote!")

    
if-else statement: The if-else statement is used to execute one block of code if a condition is True and another block of code if the condition is False.

syntax :
if (condition):
    # code of block
else:
    # code of block

Example :
score = 25

if score >= 35:
    print("You are pass")
else:
    print("You are failed")

Example :

age = 24

if (age >= 18):
    print("you can donate")
else:
    print("You can not donate")

Example :
x = 3
if x % 2 == 0:
    print("x is even")
else:
    print("x is odd")

    
if-elif-else statement: The if-elif-else statement allows you to test multiple conditions one by one and execute the block of code associated with the first True condition. If none of the conditions are True, the else block is executed.

if condition1:
    # Code to execute if condition1 is True
elif condition2:
    # Code to execute if condition2 is True
elif condition3:
    # Code to execute if condition3 is True
    .
    .
    .
elif conditionn:
    # Code to execute if conditionn is True
else:
    # Code to execute if none of the conditions are True

Example :
x = 5
if x < 0:
    print("x is negative")
elif x == 0:
    print("x is zero")
else:
    print("x is positive")


score = 113

if (score >= 0 and score <= 100):
    if (score >= 80):
        print("First class")
    elif (score >= 60):
        print("second class")
    elif (score >=40):
        print("third class")
    else:
        print("Sorry!, you are failed")
else:
    print("In-valid score \nplease enter your score between 0 to 100")

Nested if statements: You can also use if statements inside other if statements to create nested conditions.

if condition1:
    # Code for condition1 being True
    if condition2:
        # Code for condition2 being True within condition1
    else:
        # Code for condition2 being False within condition1
else:
    # Code for condition1 being False

age = int(input("Enter your age : ")) 


if (age >= 18):
    weight = int(input("Enter your weight : "))
    if weight >= 50:
        print("You can donate")
    else:
        print("You can not donate because of your weight is less than 50")
else:
    print("You can not donate because of your age is less than 18")


"""




