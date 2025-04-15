"""
Python Classes
  An object is simply a collection of data (variables) and methods (functions).
  Similarly, a class is a blueprint for that object.

Classes are user defined blueprint(logical Entity) or prototype, where we can perform diff operations
Class is a definition block which contains methods, class variables, instance variables, Constructor etc.
Class is collection of variables(attribute/state) & methods(behaviour)


Object:-
Object is instance o    f class
Object occupy certain amount in the memory
Class is logical entity & Object is physical Entity
For 1 class we can create any no of objects
Object are independent

"""


# # define a class
# class Employee:
#     # define a property
#     employee_id = 0
#
# # create two objects of the Employee class
# employee1 = Employee()
# employee2 = Employee()
#
# # access property using employee1
# employee1.employee_id = 1001
# print(f"Employee ID: {employee1.employee_id}")
#
# # access properties using employee2
# employee2.employee_id = 1002
# print(f"Employee ID: {employee2.employee_id}")


# #Example 2
#
# a=2
# b=4
# class Calculator:
#     num1=10
#     num2=20
#
#     def add(self):
#         num=self.num1+self.num2
#         print(num)
#
#     @staticmethod
#     def mul():
#         num=a.num1 * a.num2
#         print(num)
#
#     @staticmethod
#     def sub(c,d):
#         num = c * d
#         print(num)
#
# a=Calculator()
# a.add()
# Calculator.mul()
# Calculator.sub(2,3)

# # Ex3: class variable & use of self keyword
#
# # A class variable is a variable that is shared by all objects of a class.
# # It is defined inside the class but outside any method.
#
# class Sample4:
#     num1=10     # class variable -> variable which is declared inside class
#     num2=20
#
#     def add1(self):
#         print(self.num1+self.num2)
#
#     def add2(self):
#         num3=30                             #local variable
#         print(self.num1+self.num2+num3)
#
#     def add3(self,num4):                    #num= local variable
#         print(self.num1+self.num2+num4)
#
#     def mult(self):
#         print(self.num1 * self.num2)
#
# s4=Sample4()
# s4.add1()
# s4.add2()
# s4.add3(50)
# s4.mult()

#Inside Constructor by using self variable:

class Employee:
        def __init__(self):
            self.eno=100
            self.ename='Durga'
            self.esal=10000
e=Employee()
print(e.__dict__)


# Inside Instance Method by using self variable
class Test:
	def __init__(self):
		self.a=10
		self.b=20
	def m1(self):
		self.c=30
t=Test()
t.m1()
print(t.__dict__)


#Outside of the class by using object reference variable:

class Test:
	def __init__(self):
		self.a=10
		self.b=20
	def m1(self):
		self.c=30
t=Test()
t.m1()
t.d=30
print(t.__dict__)

print("--------------------------")

class Test:
	def __init__(self):
		self.a=10
	def m1(self):
		self.b=30
t1=Test()
t2=Test()
t1.m1()
t2.m1()
print(t1.a,t1.b)
print(t2.a,t2.b)
t1.a=30
t1.b=40
print(t1.a,t1.b)
print(t2.a,t2.b)

