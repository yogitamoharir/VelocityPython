"""Python Tuple
A tuple is a collection similar to a Python list. The primary difference is that
we cannot modify a tuple once it is created.

Tuple Characteristics
Tuples are:

Ordered - They maintain the order of elements.
Immutable - They cannot be changed after creation.
Allow duplicates - They can contain duplicate values.
"""

# languages = ('Python', 'Swift', 'C++')
#
# # access the first item
# print(languages[0])   # Python
#
# # access the third item
# print(languages[2])
#
# print("-------------------")
#
# cars = ('BMW', 'Tesla', 'Ford', 'Toyota')
#
# # trying to modify a tuple
# cars[0] = 'Nissan'  # error
#
# print(cars)
#
# print("-------------------")
#
# cars = ('BMW', 'Tesla', 'Ford', 'Toyota')
# print('Total Items:', len(cars))
#
# # Output: Total Items: 4

tp1 = (4, "abc", 65.1, 5, 6, 6)
print(len(tp1))
print(tp1[1])

print("-------------")

for i in tp1:
    print(i)


