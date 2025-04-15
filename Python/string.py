greet = "Hello,how are you today      "
name = "Jack"


# using + operator
# result = greet + name
# print(result)

print("------Upper()-----------")
#1. upper() 	Converts the string to uppercase
grt=greet.upper()
print(grt)


print("------lower()-----------")
#2. lower()	Converts the string to lowercase
grt=greet.lower()
print(grt)

# print("------partition-----------")
# #3. partition()	Returns a tuple
# grt.partition('are')
# print(grt)

print("------Replace()-----------")
#4. replace()	Replaces substring inside
grt=greet.replace("how","now")
print(grt)

# 5. find()	Returns the index of the first occurrence of substring
message = 'Python is a fun programming language'

# check the index of 'fun'
print(message.find('fun'))
print(greet.rfind("o"))

# Output: 12

#6.  rstrip()	Removes trailing characters
random_string = 'this is good    '

# Trailing whitespace are removed
print(random_string.rstrip())

#7. split()	Splits string from left
random_string = 'this is good, but ! i dont like   '

# Trailing whitespace are removed
# print(random_string.split(','))
print(random_string.split('!'))


#8. startswith()	Checks if string starts with the specified string
message = 'Python is fun'

# check if the message starts with Python
print(message.startswith('Python'))         # Output: True
# print(message.startswith('kython'))       # Output: False


#9.  isnumeric()	Checks numeric characters
dtr="312"
# dtr="python3.12"
print(dtr.isnumeric())
print(dtr.isnumeric())

# 10. index()	Returns index of substring
random_string = 'this is good, but ! i dont like '

index_num=random_string.index('good')
print(index_num)


## 11. isalnum()--- the is key return true or false

# string contains either alphabet or number
name1 = "Python3"

print(name1.isalnum()) #True

# string contains whitespace
name2 = "Python 3"

print(name2.isalnum()) #False

#12. isalpha()
name = "Monica"
print(name.isalpha())

# contains whitespace
name = "Monica Geller"
print(name.isalpha())

# contains number
name = "Mo3nicaGell22er"
print(name.isalpha())

print("----isdecimal()----")
#13.isdecimal() True if all characters in the string are decimal characters.

s = "28212"
print(s.isdecimal())

# contains alphabets
s = "32ladk3"
print(s.isdecimal())

# contains alphabets and spaces
s = "Mo3 nicaG el l22er"
print(s.isdecimal())

print("--------isdigit()----------")

str1 = '342'
print(str1.isdigit())

str2 = 'python'
print(str2.isdigit())

print("--------islower()----------")
s = 'this is good'
print(s.islower())

s = 'th!s is a1so g00d'
print(s.islower())

s = 'this is Not good'
print(s.islower())


print("----isnumeric-----")

pin = "523"

# checks if every character of pin is numeric
print(pin.isnumeric())

# Output:

print("----isprintable----------")
text1 = 'python programming'

# checks if text1 is printable
result1 = text1.isprintable()
print(result1)

text2 = 'python programming\n'

# checks if text2 is printable
result2 = text2.isprintable()
print(result2)


print("-----isspace()---------")
s = '   \t'
print(s.isspace())

s = '    a   '
print(s.isspace())

s = ''
print(s.isspace())

print("-----istitle---------")

s = 'Python Is Good.'
print(s.istitle())

s = 'Python is good'
print(s.istitle())

s = 'This Is @ Symbol.'
print(s.istitle())

s = '99 Is A Number'
print(s.istitle())

s = 'PYTHON'
print(s.istitle())

print("-------issuper()------")

# example string
string = "THIS IS GOOD!"
print(string.isupper());

# numbers in place of alphabets
string = "THIS IS ALSO G00D!"
print(string.isupper());

# lowercase string
string = "THIS IS not GOOD!"
print(string.isupper());

print("-------.join()-------")

text = ['Python', 'is', 'a', 'fun', 'programming', 'language']

# join elements of text with space
print(' '.join(text))

# Output: Python is a fun programming language

#example 2
# .join() with lists
numList = ['1', '2', '3', '4']
separator = ', '
print(separator.join(numList))

# .join() with tuples
numTuple = ('1', '2', '3', '4')
print(separator.join(numTuple))

s1 = 'abc'
s2 = '123'

# each element of s2 is separated by s1
# '1'+ 'abc'+ '2'+ 'abc'+ '3'
print('s1.join(s2):', s1.join(s2))

# each element of s1 is separated by s2
# 'a'+ '123'+ 'b'+ '123'+ 'b'
print('s2.join(s1):', s2.join(s1))


print("---swapcase----")
name = "JoHn CeNa"

# converts lowercase to uppercase and vice versa
print(name.swapcase())

# Output: jOhN cEnA

print("--------strip--------")

message = '     Learn Python  '

# remove leading and trailing whitespaces
print(message.strip())

# Output: Learn Python


print("---splitlines---")

# \n is a line boundary
sentence = 'I\nlove\nPython\nProgramming.'

# returns a list after spliting string at line breaks
resulting_list = sentence.splitlines()

print(resulting_list)

# Output: ['I', 'love', 'Python', 'Programming.']


print("---------------------Velocity teaching-------------------------------")



s1="velocity"
s2="ABCD"
s3="abcd"
s4="my name is abc"
s5="abcaba"             #   0-5



print("-------")
print(s1[3])            # o
print(s1[2:5])          # 2-4  #s1[startIndex:endIndex+1]

print(s5.find('b'))          # returns index of 1st occurrence chars
print(s5.index('b'))         # Alternate way

print(s5.rfind('b'))          # returns index of last occurrence chars
print(s5.rindex('b'))         # Alternate way
print("----------")
print(len(s1))

s1=s1.upper()       #Re-Initialization
print(s1)
print(s1.upper())
print(s1)

s2=s2.lower()
print(s2)
print(s2.lower())
print(s2)

print(s2==s3)                        #compare data & case
print(s2.__eq__(s3))                #compare data & case        #Alternate way
print(s2.lower()==s3.lower())        #compare only data

print("--------")

print("is" in s4)
print(s4.__contains__("is"))  #Alternate way

print(s4.startswith("my"))
print(s4.endswith("Abc"))



s1="abc"
s2="xyz"
s3="  abcd   "
s4="my name is abc"

print(s1+s2)      #abcxyz

print(s3.strip())
print(s3.lstrip())
print(s3.rstrip())

print(s4.replace("abc","xyz"))    # my name is xyz

print("------------------")


s5="velocity"
s6="ABcd"
print(s5.capitalize())      #Velocity      convert 1st letter of string to upper case
print(s4.title())           #My Name Is Abc
print(s6.swapcase())        #abCD

print("----------")
#
str1="123"
str2="abc123"
str3="  "
str4="my name is abc is abc is"

print(s5.isalpha())             #True
print(str1.isdigit())           #True
print(str2.isalnum())           #True
print(str3.isspace())             #True

print(str4.count("abc"))
