#  List
# It like array/ArrayList
# It can be homogeneous or heterogeneous
#
#
# •	List can contain duplicate items.
# •	List in Python are Mutable. Hence, we can modify, replace or delete the items.
# •	List are ordered. It maintains the order of elements based on how they are added.
# •	Accessing items in List can be done directly using their position (index), starting from 0.
#
# —------Example of List-------

ls= [6, 5,0,"abc", 11.5]

# get size of list
print(len(ls))

# get specific data
print(ls[1])

#------adding elements----------
ls.append(4)
print(ls)

# add elements to specific index
ls.insert(3, 10)
print(ls)
print(ls[3])

# add multiple element
ls.extend([-5, -6])
print(ls)

# Remove elements by index
ls.pop(1)  # Removes element at index 1
print(ls)
ls.pop()    # Remove element from last in
print(ls)

# Remove any object
ls.remove(11.5)
print(ls)

#---copy list—--
ls1 = ls.copy()
print(ls1)

#-------------Sorting—-----------
#Ascending order
lst2 = [3, 1, 4, 2]
lst2.sort()  	# [1, 2, 3, 4]
print(lst2)

#Descending order
lst2.reverse()  # [4, 3, 2, 1]
print(lst2)

#Sort list without changing original list
#returns new list without modifying # original list
new_list = sorted(lst2)
print(new_list)


# Searching & Counting
lst = [1, 4, 8, 6, 4, 6, 2,8]
print(lst.index(8))  # returns 1st occu

lst = [1, 2, 2, 3, 2]
print(lst.count(2))  # find total oc of ele

#clear list
#lst.clear()  # [] remove all elements

#delete list
del lst # Deletes the list entirely
print(lst)   #error


# Searching & Counting
lst = [1, 4, 8, 6, 4, 6, 2,8]
print(lst.index(8))  # returns 1st occu

lst = [1, 2, 2, 3, 2]
print(lst.count(2))  # find total oc of ele



