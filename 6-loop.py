"""
Loops in Python are control structures that allow you to repeatedly execute a block of code as long as a specified condition is True or for a specific number of iterations. Python has two main types of loops: for loops and while loops

For Loops: For loops are typically used when you have a sequence (such as a list, tuple, or string) or an iterable object, and you want to iterate over each item in the sequence one by one.

syntax:
for ele in iterable:
    # Code to be executed for each item

range(start, end-1, step-1)

for num in list(range(1,21)):
    print(num)

While Loops: While loops are used when you want to repeat a block of code as long as a certain condition remains True.

syntax : 
while condition:
    # Code to be executed while the condition is True

count = 0
while count < 5:
    print(count)
    count += 1

Example : 

while(True):
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
# num = 5

# for r in range(1, num+1):
#     for c in range(1, num+1):
#         print(c, end=" ")
#     print("\n")
    
# 1 2 3 4 5

# 1 2 3 4 5

# 1 2 3 4 5

# 1 2 3 4 5

# 1 2 3 4 5


# num = 5

# for r in range(1, num+1):
#     for c in range(1, r+1):
#         print(" *", end=" ")
#     print("\n")
    


# print(list(range(10, 0, -1)))

# num = 10

# for r in range(num, 0, -1):
#     for c in range(r):
#         print(" *", end=" ")
#     print("\n")



# num = 10

# for r in range(num, 0, -1):
#     for c in range(num, 0, -1):
#         print(" *", end=" ")
#     print("\n")






# table = 50
# start = 1
# while (start <= 10):
#     print(f"{table} * {start} = {table * start}")
#     start += 1