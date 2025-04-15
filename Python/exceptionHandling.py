
				# Exception Handling

# print("Program started")
# a=10
# b=0
#
# print(a/b)      #10/0  = 5          #risky code
#
# print("Program ended")


print("-----Ex1.1: basic example of Exception handling------")
print("Program started")
a=10
b=0

try:
    print(a / b)  # 10/0  = error          #risky code
except ZeroDivisionError as e:
    print("ZeroDivision Error handled - divide by zero operation not possible in python")

print("Program ended")

print("-----1.2: basic example of Exception handling -> With Alternate code------")
print("Program started")
a=10
b=0

try:
    print(a / b)  # 10/0  = error          #risky code
except ZeroDivisionError as e:
    print(a/1)                              #Alternate code

print("Program ended")

print("-----1.3: basic example of Exception handling------")
print("Program started")
a=10
b=0

try:
    print(a / b)  # 10/0  = error          #risky code
except ZeroDivisionError:
    print("Exception Handled")

print("Program ended")





print("-----2: Multiple Except block for 1 try block------")
print("Program started")
a=10
b=0

try:
    print(a / b)                #risky code
except ValueError:
    print("ValueError Handled")
except ZeroDivisionError:
    print("ZeroDivisionError handled")
except AssertionError:
    print("AssertionError handled")

print("Program ended")


print("-----Ex3: Generic Exception------")
print("Program started")
a=10
b=0
try:
    print(a / b)                #risky code
except Exception as e:
    print(e)
    print("Generic Exception Handled")

print("Program ended")


print("-----Ex4: Correct way of using Generic Exception------")
print("Program started")
a=10
b=0
try:
    print(a / b)                #risky code
except ValueError:
    print("ValueError Handled")
except AssertionError:
    print("AssertionError handled")
except Exception as e:
    print(e)
    print("Generic Exception Handled")

print("Program ended")



print("-----Ex5: adding multiple exception in one Exception------")

# name="Yogita"
# # print(namee)
# try:
#     print(namee)
# except (ValueError,AssertionError,ZeroDivisionError):
#     print("Error occured but Handled")
# except NameError as e:
#     print(e)
# except Exception as e:
#     print(e)

print("---------start-------")
count=2
if count==2:
    raise Exception ("exception for count ==2")
