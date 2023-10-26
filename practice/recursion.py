# 5

# 5 * 4 * 3 * 2 * 1 = 120

def fact(num):
    if num == 1:
        return 1
    else:
        return num * fact(num-1)

number = input("Enter a number: ")
print(fact(int(number)))