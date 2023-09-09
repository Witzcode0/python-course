"""
Operators are special symbols or keywords that are used to perform various operations on values and variables. Python supports a wide range of operators, which can be categorized into several types:
"""

# 1] Arithmetic Operators:
print("\n\nArithmetic Operators")
"""
+ (Addition): Adds two values.
- (Subtraction): Subtracts the right operand from the left operand.
* (Multiplication): Multiplies two values.
/ (Division): Divides the left operand by the right operand.
% (Modulus): Returns the remainder of the division.
** (Exponentiation): Raises the left operand to the power of the right operand.
// (Floor Division): Returns the floor of the division (result without the fractional part).
"""


x = 10
y = 20

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)



# 2] Assignment Operators:
print("\n\nArithmetic Operators")
"""
= (Assignment): Assigns a value to a variable.
+= (Add and Assign): Adds the right operand to the left operand and assigns the result to the left operand.
-= (Subtract and Assign): Subtracts the right operand from the left operand and assigns the result to the left operand.
*= (Multiply and Assign): Multiplies the left operand by the right operand and assigns the result to the left operand.
/= (Divide and Assign): Divides the left operand by the right operand and assigns the result to the left operand.
%= (Modulus and Assign): Applies modulus to the left operand with the right operand and assigns the result to the left operand.
**= (Exponentiate and Assign): Raises the left operand to the power of the right operand and assigns the result to the left operand.
//= (Floor Division and Assign): Applies floor division to the left operand by the right operand and assigns the result to the left operand.
"""
a = b = c = d = e = f = g = 10
# a = a + 20
a += 20
print(a)
b -= 20
print(b)
c *= 20
print(c)
d /= 20
print(d)
e %= 20
print(e)
f **= 20
print(f)
g //= 20
print(g)

# 3] Comparison/Conditional Operators:
print("\n\nComparison Operators")
"""
== (Equal): Checks if two values are equal.
!= (Not Equal): Checks if two values are not equal.
< (Less Than): Checks if the left operand is less than the right operand.
> (Greater Than): Checks if the left operand is greater than the right operand.
<= (Less Than or Equal To): Checks if the left operand is less than or equal to the right operand.
>= (Greater Than or Equal To): Checks if the left operand is greater than or equal to the right operand.
"""
x = 10
y = 20
z = 10

print(x == y) # False
print(x != z) # False
print(x < y) # True
print(z > y) # False
print(x <= z) # True
print(x >= y) # False

# 4] Logical Operators:
print("\n\nLogical Operators")
"""
and (Logical AND): Returns True if both operands are True.
or (Logical OR): Returns True if at least one operand is True.
not (Logical NOT): Returns the opposite of the operand's truth value.

A B C   and or
T T F   F   T
T F T   F   T
F T T   F   T
T T T   T   T
F F F   F   F
"""
a = True
b = False
c = 3 < 5
d = 5 < 1

# and
print(a and b and d) # False

# or
print(c or d) # True
print(b or d) # False

# not
print(not a) # False
print(not b) # True

# 5] Membership Operators:
print("\n\nMembership Operators")
"""
in: Checks if a value is present in a sequence (e.g., a list, tuple, or string).
not in: Checks if a value is not present in a sequence.
"""

name = "Molmeh Technolabs"
print('m' in name) # True
print("TH" in name) # False
print("ola" not in name) # False

# 6] Identity Operators:
print("\n\nIdentity Operators")
"""
is: Checks if two variables refer to the same object in memory.
is not: Checks if two variables do not refer to the same object in memory.
"""

x = 10
y = 20
z = 20

print(x is y) # False
print(x is not y) # True
print( y is not z) # False
