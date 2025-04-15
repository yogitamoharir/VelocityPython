
# Functions in Python

# A function in Python is a reusable block of code that performs a specific task.
# It can take inputs (parameters), execute code, and return a result.
# Functions help in organizing and reusing code efficiently.



# 1: Function Without parameter
def m1():               #function declaration
    print("hi")         # function body
    print("hello")
    print("GM")

m1()                #function call    -> functionName()
m1()                #code reusability

print("---------------")
def addition():
    num1=10
    num2=20
    print(num1+num2)

addition()
addition()

print("-------------")
def sub():
    num1=40
    num2=250
    print(num1-num2)

sub()

# Function With Parameter

print("-------Ex1: With 1 int parameter--------")
def findSquareOfNum(num1):
    print(num1*num1)

findSquareOfNum(5)
findSquareOfNum(7)


print("-------Ex2: With 2 int parameter--------")
def addition(num1, num2):           #num1=50, num2=60    2 para Fun
    print(num1+num2)                #

addition(10,20)
addition(50,60)
addition(100,200)


print("------Ex3: With 1 String parameter-------")
def studentName(name):
    print(name)

studentName("Amol")
studentName("Ganesh")

print("------Ex4: With multiple parameter of diffrent types--------")
def studentInfo(name,rollNum, percentage,grade):
    print("Student Name: ",name)
    print("Student Roll Num: ",rollNum)
    print("Student Percentage: ",percentage)
    print("Student Grade: ",grade)

studentInfo("Amol",101,65.1,"A+")
print("------")
studentInfo("Mahesh",102,55.1,"B+")


print("--------Ex5: Positional parameter: ---------")
def greet(name, age):
    print("My Name is: ",name)
    print("My Age is: ", age)

# Calling the function with positional arguments
greet("abc", 25)  # Correct order
greet(25, "Alice")  # Incorrect order, meaning changes


print("------Ex6: Keyword parameter(Order/position doesn't matter)------")
def greet(name, age):
    print("My Name is: ",name)
    print("My Age is: ", age)

# Calling the function using keyword arguments
greet(name="xyz1", age=25)
greet(age=30, name="xyz2")  # Order doesn't matter


print("------Ex7: Default/optional parameter------")
def greet(name="abc", age=10):          #providing default vaules to the variables
    print("My Name is: ",name)
    print("My Age is: ", age)

greet()
print("---")
greet("xyz",20)


print("------Function example with return-----")
#-------------Function with return--------------

def add(num1,num2):
    addition=num1+num2
    return addition

sum=add(7,8)
print(sum)
