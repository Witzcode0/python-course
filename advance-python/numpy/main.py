import numpy as np

# print(np.__version__)

# a = np.array([1,2,3,4,5])
# print(type(a))

# 0 - D
# a = np.array(50)
# print(a.ndim)

# 1 - D
# a = np.array([50])
# print(a.ndim)

# indexing
# print(a[0])

# 2 - D
# a = np.array([[50,20,30],[10,40,70]])
# print(a.ndim)
# print(a[0][1])


# a = np.array([[1,2,3,4,5],[6,7,8,9,10]])
# # print(a.ndim)
# print(a[1, 4])

# 3 - D
# a = np.array([[[1,2,3,4,5],[6,7,8,9,10]]])
# print(a[0, 0, 3])
# print(a[0][1,-1])

# slicing
# a = np.array(['a', 'b', 'c', 'd', 'e', 'f'])
# print(a[1:3])
# print(a[4:])
# print(a[-3:-1])


# a = np.array([[1,2,3,4,5],[6,7,8,9,10]])
# print(a[1, 1:4])
# print(a[0:2, 1:4])

# datatypes

# a = np.array([1,2,3,4,5])
# a = np.array(['a','b','c'])
# print(a.dtype)

# a = np.array([23.50, 45.89898, 0.2356462354362, 12.3746873462])
# # print(a.dtype)
# new_a = a.astype('i')
# print(new_a)
# print(new_a.dtype)

# num = int(input("Enter dim: "))
# a = np.array([1,2,3,4,5], ndmin=num)
# print(a)
# print(a.ndim)

# a = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# new_a = a.reshape(2,6)
# print(new_a)