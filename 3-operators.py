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

# 7] Bitwise Operators
print("\n\nBitwise Operators")
"""
Bitwise operators in Python are used to perform operations at the bit level of binary numbers. These operators manipulate individual bits of integers or binary numbers. Python provides the following bitwise operators:
"""
# Decimal	
# 2^7 = 128	
# 2^6 = 64	
# 2^5 = 32	
# -----------
# 2^4 = 16	
# -----------
# 2^3 = 8	
# 2^2 = 4	
# 2^1 = 2
# 2^0 = 1

# Dec 3 -> Bin 0 0 1 1
# Dec 5 -> Bin 0 1 0 1
# Dec 18 -> Bin 1 0 0 0 1 0

"""
Bitwise AND (&):

The & operator performs a bitwise AND operation between corresponding bits of two integers.
If both bits are 1, the result is 1; otherwise, it's 0.
"""
a = 5  # binary: 0101
b = 3  # binary: 0011
result = a & b  # result: 0001 (decimal 1)
print(result)


"""
Bitwise OR (|):

The | operator performs a bitwise OR operation between corresponding bits of two integers.
If at least one bit is 1, the result is 1; otherwise, it's 0.
"""
a = 5  # binary: 0101
b = 3  # binary: 0011
result = a | b  # result: 0111 (decimal 7)
print(result)

"""
Bitwise XOR (^):

The ^ operator performs a bitwise XOR (exclusive OR) operation between corresponding bits of two integers.
If the bits are different (one is 0 and the other is 1), the result is 1; otherwise, it's 0.
"""
a = 5  # binary: 0101
b = 3  # binary: 0011
result = a ^ b  # result: 0110 (decimal 6)
print(result)


"""
Bitwise NOT (~):

The ~ operator performs a bitwise NOT operation on an integer, which means it inverts all the bits.
1s become 0s, and 0s become 1s.
"""

a = 5  # binary: 0101
result = ~a  # result: 1010 (decimal -6)
print(result)

"""
Bitwise Left Shift (<<):

The << operator shifts the bits of an integer to the left by a specified number of positions.
It effectively multiplies the integer by 2 raised to the specified power.
"""

a = 5  # binary: 0101
result = a << 2  # result: 20 (binary: 10100)
print(result)


# x = 7 - 00000111 = 7
# x = x << 1 - 00001110 = 14
# x = x << 3 - 01110000 = 112
# x = x << 2 - 11000000 = 192


"""
Bitwise Right Shift (>>):

The >> operator shifts the bits of an integer to the right by a specified number of positions.
It effectively divides the integer by 2 raised to the specified power.
"""
a = 20  # binary: 10100
result = a >> 2  # result: 5 (binary: 0101)
print(result)