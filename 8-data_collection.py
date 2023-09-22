"""
In Python, data collection typically refers to the process of gathering and storing data from various sources and in various data structures. Data collection is a fundamental step in data analysis, processing, and manipulation. 

List : - ordered, mutable, allow duplicate value
Lists are one of the most commonly used data structures in Python for collecting and storing data. They are ordered and mutable, which means you can add, remove, and modify elements in a list.

syntax : 
list_name = []
list_name = list()


Tuple :ordered, immutable, allow duplicate values
Tuples are similar to lists but are immutable, which means you cannot change their elements once they are assigned. Tuples are often used to collect related data that should not change.

syntax : 
tuple_name = ()
tuple_name = tuple()
tuple_name = 1,



Set : unordered, mutable, not allow duplicate values
Sets are used to collect a collection of unique elements. They do not allow duplicate values and are useful when you want to perform set operations like union, intersection, etc.

syntax : 

set_name = {1,2,3,7}

Dictionary : ordered, mutable, dupplicate key is not allow
Dictionaries are collections of key-value pairs. They are used to store and retrieve data based on a unique key.

dict_name = {
    'key':'value',
    'key':'value',
    'key':'value',
    'key':'value',
    'key':'value',
}
"""

int_list = [1, 2, 3, 4, 5]
float_list = [12.3, 23.5, 45.67, 27.78, 89.1]
str_list = ["str1", "str2", 'str3', 'str4', 'str5']

mix_list = [12, 34.5, "test"]

# print(type(mix_list)) # <class 'list'>

# print(len(mix_list)) # 3


# access element of list
# mix_list = mix_list + int_list + float_list + str_list

# print(mix_list)

# concat
# new_list = int_list + str_list
new_list = [1, 2, 3, 4, 5, 'str1', 'str2', 'str3', 'str4', 'str5']

# indexing(+)
# print(new_list[5])
# print(new_list[2])

# indexing(-)
# print(new_list[-3])
# print(new_list[-8])

# slicing(range)
# sequence_name[start:end:step]
# print(new_list[5:8])
# print(new_list[::-1])
# print(new_list[-5::])

# duplicate data list

# nums = [1,1,1,2,1,4,1,5,5,6]

# print(nums)

# methods of list
products = ['p1','p2','p3','p4','p5']

# print(dir(products))

# 'append', 'extend', 'insert'
# new_products = ['p6','p7']
# products.append(new_products) # ['p1', 'p2', 'p3', 'p4', 'p5', ['p6', 'p7']]
# products.extend(new_products) # ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7']
# products.insert(0, new_products) # [['p6', 'p7'], 'p1', 'p2', 'p3', 'p4', 'p5']


# 'clear', 'pop', 'remove',
# products.clear() # []
# products.pop() # ['p1', 'p2', 'p3', 'p4']
# products.remove("p4") # ['p1', 'p2', 'p3', 'p5']


# 'copy', 
# copy_list = []
# copy_list = products.copy() # ['p1', 'p2', 'p3', 'p4', 'p5']
# print(copy_list)


# 'count',  
# print(products.count("p1"))


# 'index',  
# print(products.index('p4')) # 3

# 'reverse', 'sort'
# products.reverse()
# products.sort()
# print(products)


# for p in products:
#     print(p)


# Nested list
# nested_list = [10,20, [30,40, [50, 60]]]
# print(nested_list)
# print(nested_list[2])
# print(nested_list[2][2])
# print(nested_list[2][2][0])



# t = ()
# t = tuple()
# t = 1,2,3,4
# print(type(t))

# int_tuple = (1,1,2,3,4,5,1)
# print(dir(int_tuple))

# 'count', 'index'

# print(int_tuple.count(1))
# print(int_tuple.index(5))

# indexing(+)
# print(int_tuple[2])

# indexing(-)
# print(int_tuple[-2])

# slicing
# print(int_tuple[2:])

# int_tuple[1] = "test" # TypeError: 'tuple' object does not support item assignment

# print(int_tuple) 


# set

# i_set = {1,1,2,3,4,5,1}
# print(type(i_set))

# print(dir(i_set))

# print(i_set) # {1, 2, 3, 4, 5}

# print(i_set[0])  # TypeError: 'set' object is not subscriptable

# i_set.add("111")

# frozenset

# i_set = frozenset(i_set)
# i_set.add("112")
# print(i_set)



user = {
    'name':"brijesh",
    'age':27,
    'mobile':['9898989898', "54654645656"],
    'name':"jay"
}

# print(type(user))

# print(dir(user))

# print(user['name'])
# print(user['age'])
# print(user['mobile'][1])

# print(user)

# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'

# print(user.get('name'))

# print(user.items())
# print(user.keys())
# print(user.values())

# user.popitem()
# user.pop("age")


# print(user)

# user.clear()
# print(user) # {}

# d = {}

# d = user.copy()

# print(id(d))
# print(id(user))

# a = b = 10

# print(id(a) == id(b))

# assign_property = {}

# l = ['child1', 'child2', 'child3']
# property = 50/len(l)

# x = assign_property.fromkeys(l, property)
# print(x)


# car = {
#     "name":"BMW",
#     "price":"20l",
#     "color":"red"
# }

# car.setdefault("color", "blue")
# car.setdefault("model", "xyz")
# print(car)

users = {}

person_info = {
    "name":"brijesh",
    "age":27
}

edu_info = {
    "degree":"BE[IT]"
}

contact_info = {
    'email':"brijesh@gmail.com",
    'mobile':8980145007
}

users.update(person_info)
users.update(edu_info)
users.update(contact_info)
print(users)


for k, v in users.items():
    print(k, v)