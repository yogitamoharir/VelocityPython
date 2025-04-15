"""
Python List
In Python, lists allow us to store multiple items in a single variable.
For example, if you need to store the ages of all the students in a class,
you can do this task using a list.

Lists are similar to arrays (dynamic arrays that allow us to store items of
different data types) in other programming languages.

List Characteristics
In Python, lists are:

Ordered - They maintain the order of elements.
Mutable - Items can be changed after creation.
Allow duplicates - They can contain duplicate values.

"""
## Methods of list
#1.append
fruits = ['apple', 'banana', 'orange']

fruits.append("cherry")
print(fruits)

#extend
veggy=["flower","ocra","bottle Guard"]
fruits.extend(veggy)
print(fruits)

#insert
veggy=["flower","ocra","bottle Guard"]
veggy.insert(2,"snake guard")
print(veggy)

#remove
veggy=["flower","ocra","bottle Guard"]
veggy.remove("ocra")
print(veggy)

#pop
veggy=["flower","ocra","bottle Guard"]
# veggy.pop()   ##without index
veggy.pop(2)   #with index
print(veggy)

#clear
veggy=["flower","ocra","bottle Guard"]
# veggy.clear()
# print(veggy)

#index
veggy=["flower","ocra","bottle Guard"]
item_num=veggy.index("bottle Guard")
print(item_num)

#count
veggy=["flower","ocra","bottle Guard","bottle Guard","bottle Guard"]
item_num=veggy.count("bottle Guard")
print(item_num)

#sort
veggy=["flower","ocra","bottle Guard","bottle Guard","bottle Guard"]
veggy.sort()
print(veggy)    #sort will sort original list


#copy
veggy=["flower","ocra","bottle Guard","bottle Guard","bottle Guard"]
veg_copy=veggy.copy()
print(veg_copy)


#reverse
veggy=["flower","ocra","bottle Guard","bottle Guard","bottle Guard",2,3,45]
veggy.reverse()
print(veggy)











