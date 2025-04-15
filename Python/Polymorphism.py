"""
PolyMorphism

It is one of the OOPs principles where one object shows different behaviour at different stages
of life cycle.
Polymorphism is a Latin word where poly stands for many & morphism stands for forms.
PolyMorphism-> 1 Object many form
Shape -> circle, Square, Rectangle

"""
print(5+5)
print("5"+"5")   #same function[print()] diff behaviour
print("-------------------")
s1="abcd"
print(len(s1))
l1=["abc",10,55.1]      #same function[len()] diff behaviour
print(len(l1))


"""
How to Achieve PolyMorphism in Python:
Method Overriding:
Method Overloading
Method Overriding:
The sub/derived class provides a specific implementation of a method that is already 
defined in its base class or parent class.
Before performing Method Overriding, 1st we need to perform inheritance

##Method Overriding in Python Inheritance:
In this case, the method in the subclass overrides the method in the superclass.
This concept is known as method overriding in Python.
"""

class Animal:
    # attributes and method of the parent class
    name = ""
    def eat(self):
        print("I can eat")
# inherit from Animal
class Dog(Animal):
    # override eat() method
    def eat(self):
        print("I like to eat bones")
# create an object of the subclass
labrador = Dog()
# call the eat() method on the labrador object
labrador.eat()


"""
The super() Function in Inheritance
Previously we saw that the same method (function) in the subclass
overrides the method in the superclass.
However, if we need to access the superclass method from the 
subclass, we use the super() function.
"""

class Animal:
    name = ""
    def eat(self):
        print("I can eat")
# inherit from Animal
class Dog(Animal):
    # override eat() method
    def eat(self):
        # call the eat() method of the superclass using super()
        super().eat()
        print("I like to eat bones")
# create an object of the subclass
labrador = Dog()
labrador.eat()


"""
Method Overloading:
Declaring multiple method with same method name but with different argument/parameter/inputs
in a same class is called method overloading
PolyMorphism concept we can implement using overloading concept
Not completely supported in python just like java, somehow we can achieve polymorphism

"""

# EX1:
class Demo:
 def add(self,a=0, b=0,c=0,d=0):
     print(a+b+c+d)
d=Demo()
d.add()
d.add(10,20)
d.add(10,20,30)
d.add(10,20,30,40)

# EX2:
class Sample:
 def printName(self,sName="xyz"):
    print(sName)
s=Sample()
s.printName()
s.printName("Mahesh")