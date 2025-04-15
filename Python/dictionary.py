"""
Python Dictionary
A Python dictionary is a collection of items, similar to lists and tuples.
However, unlike lists and tuples, each item in a dictionary is a key-value pair
(consisting of a key and a value).


***************** Function	Description *********
pop()	Removes the item with the specified key.
update()	Adds or changes dictionary items.
clear()	Remove all the items from the dictionary.
keys()	Returns all the dictionary's keys.
values()	Returns all the dictionary's values.
get()	Returns the value of the specified key.
popitem()	Returns the last inserted key and value as a tuple.
copy()	Returns a copy of the dictionary.

"""

##Access Dictionary Items

country_capitals = {
  "Germany": "Berlin",
  "Canada": "Ottawa",
  "England": "London"
}

# access the value of keys
print(country_capitals["Germany"])    # Output: Berlin
print(country_capitals["England"])    # Output: London

#2.get()
print(country_capitals.get("Germany"))

#3.add item in dictionary
country_capitals["India"]= "Delhi"
print(country_capitals)

#4.remove()
del country_capitals['Germany']
print(country_capitals)

print("----------------update()------------")

#5. update() exising item in dict
country_capitals = {
  "Germany": "Berlin",
  "Italy": "Naples",
  "England": "London",
  "India": "Delhi"
}

# change the value of "Italy" key to "Rome"
country_capitals["Italy"] = "Rome"

print(country_capitals)

#6.pop()
print("---------pop()-------------")
country_capitals.pop("India")
print(country_capitals)


print("-------------keys()------------")
#7.keys()
numbers = {1: 'one', 2: 'two', 3: 'three'}

# extracts the keys of the dictionary
dictionaryKeys = numbers.keys()

print(dictionaryKeys)

# Output: dict_keys([1, 2, 3])

print("-------------values()------------")
#8.values()

numbers = {1: 'one', 2: 'two', 3: 'three'}

# extracts the keys of the dictionary
dictionaryValues = numbers.values()

print(dictionaryValues)

#Iterate Through a Dictionary

country_capitals = {
  "United States": "Washington D.C.",
  "Italy": "Rome"
}

# print dictionary keys one by one
for country in country_capitals:
    print(country)

print()

# print dictionary values one by one
for country in country_capitals:
    capital = country_capitals[country]
    print(capital)


print("--------------velocity-----------------")


dict1={}
dict1["firstname"]="abc"
dict1["lastname"]="xyz"
dict1["Gender"]="male"
print(dict1)
print("FN: "+dict1["firstname"])


student = {
"name": "Alice",
"age": 25,
"courses": ["Math", "Physics"],
"is_graduated": True
}
# Accessing values
print(student["name"]) # Output: Alice
print(student.get("age")) # Output: 25


# Removing the last inserted item
student.popitem() # Removes 'is_graduated'
print(student)
# Output: {'name': 'Alice', 'age': 26, 'courses': ['Math', 'Physics']}


# Accessing keys, values, and items
print(student.keys()) # Output: dict_keys(['name', 'age', 'courses'])
print(student.values()) # Output: dict_values(['Alice', 26, ['Math', 'Physics']])
print(student.items()) # Output: dict_items([('name', 'Alice'), ('age', 26), ('courses', ['Math', 'Physics'])])
# Iterating through a dictionary
for key, value in student.items():
    print(f"{key}: {value}")