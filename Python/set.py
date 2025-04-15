"""
Python Sets
A set is a collection of unique data, meaning that elements within a set cannot be duplicated.

"""
#methods in set
#1. add()
numbers = {21, 34, 54, 12}

print('Initial Set:',numbers)

# using add() method
numbers.add(32)

print('Updated Set:', numbers)

#2.update()
companies = {'Lacoste', 'Ralph Lauren'}
tech_companies = ['apple', 'google', 'apple']

# using update() method
companies.update(tech_companies)

print(companies)

# Output: {'google', 'apple', 'Lacoste', 'Ralph Lauren'}

#3.discard() and clear()
companies = {'Lacoste', 'Ralph Lauren','apple','moto','realme'}
companies.discard('moto')
# companies.clear()
# companies.remove("applee")   ###throws error if the element doesn't exist
# companies.discard("applee")   ####no error even if the element doesn't exist
print(companies)

#4.copy()
new_company=companies.copy()
print("new_company",new_company)

#5.pop()
# new_company.pop()
# print(new_company)

#6. remove()
new_company.remove("apple")
print(new_company)


# 7.sorted

st3={5,20,90,1,80,7}
print(st3)
st4=sorted(st3)
print(st4)