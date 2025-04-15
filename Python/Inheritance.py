"""
Python Inheritance
Being an object-oriented language, Python supports class inheritance.
It allows us to create a new class from an existing one.

The newly created class is known as the subclass (child or derived class).
The existing class from which the child class inherits is known as the superclass
(parent or base class).

Inheritance Types
There are 5 different types of inheritance in Python. They are:

Single Inheritance: a child class inherits from only one parent class.
Multiple Inheritance: a child class inherits from multiple parent classes.
Multilevel Inheritance: a child class inherits from its parent class, which is inheriting from its parent class.
Hierarchical Inheritance: more than one child class are created from a single parent class.
Hybrid Inheritance: combines more than one form of inheritance.

"""

##Single Inheritance

class Calculator:
    # def __init__(self, num1, num2):  # Constructor to initialize num1 and num2
    #     self.num1 = num1
    #     self.num2 = num2
    num1=20
    num2=10

    def add(self):
        num = self.num1 + self.num2
        print(num)

class Math(Calculator):  # #here m1 is object of math class which inherites property of Calculator clas
    def sub(self):
        num = self.num1 - self.num2
        print(num)

# Creating an object with numbers
# m1 = Math(20,10)
m1 = Math()

m1.add()  # Output: 8
m1.sub()  # Output: 2



# Example: Python Multiple Inheritance
"""
A class can be derived from more than one superclass in Python. 
This is called multiple inheritance.

For example, a class Bat is derived from superclasses Mammal and 
WingedAnimal. It makes sense
because bat is a mammal as well as a winged animal.
"""
class Mammal:
    def mammal_info(self):
        print("Mammals can give direct birth.")

class WingedAnimal:
    def winged_animal_info(self):
        print("Winged animals can flap.")

class Bat(Mammal, WingedAnimal):
    pass

# create an object of Bat class
b1 = Bat()

b1.mammal_info()
b1.winged_animal_info()

"""
Multilevel Inheritance

In Python, not only can we derive a class from the superclass
 but you can also derive a class from the derived class.
 This form of inheritance is known as multilevel inheritance.
"""

class SuperClass:

    def super_method(self):
        print("Super Class method called")

# define class that derive from SuperClass
class DerivedClass1(SuperClass):
    def derived1_method(self):
        print("Derived class 1 method called")

# define class that derive from DerivedClass1
class DerivedClass2(DerivedClass1):

    def derived2_method(self):
        print("Derived class 2 method called")

# create an object of DerivedClass2
d2 = DerivedClass2()

d2.super_method()  # Output: "Super Class method called"

d2.derived1_method()  # Output: "Derived class 1 method called"

d2.derived2_method()  # Output: "Derived class 2 method called"

print("-----------Hirarchical-------------")
# Ex4 :Hierarchical Inheritance:
# multiple sub classes can acquire properties of 1 super class is known as hierarchical Inheritance.

class Father:
    def car(self):
        print("Running car method from super class")
    def money(self):
        print("Running Money method from super class")
    def home(self):
        print("Running Home method from super class")

class Son1(Father):
     def mobile(self):
        print("Mobile method from Son1")

class Son2(Father):
     def laptop(self):
        print("Laptop method from Son2")

print("--------Features of Son1-----")
s1=Son1()
s1.mobile()
s1.car()
s1.money()
s1.home()
print("--------Features of Son2-----")
s2=Son2()
s2.laptop()
s2.car()
s2.money()
s2.home()
