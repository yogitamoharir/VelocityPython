# if, elif, else
import random

# num=30
# if num >= 35:
#     print("pass")
# else:
#     print("fail")

# """1. Write a Python program to find those numbers which are divisible by 7 and multiples of 5,
# between 1500 and 2700 (both included).
# """
#
# count=[]
# for num in range(1500,2701):
#     if num%7==0 and  num % 5 == 0:
#         count.append(num)
# print(count)
# print(len(count))

# """
# Write a Python program to guess a number between 1 and 9.
# Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again
#  the guess is correct, on successful guess, user will get a "Well guessed!"
# message, and the program will exit.
# """
# import random
#
# # Generate a random number between 1 and 10 (inclusive) as the target number
# target_num, guess_num = random.randint(1, 10), 0
#
# # Start a loop that continues until the guessed number matches the target number
# while target_num != guess_num:
#     # Prompt the user to input a number between 1 and 10 and convert it to an integer
#     guess_num = int(input('Guess a number between 1 and 10 until you get it right : '))
#
# # Print a message indicating successful guessing once the correct number is guessed
# print('Well guessed!')


# """
# 4. Write a Python program to construct the following pattern, using a nested for loop.
#
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
# """
#
# n=5
# for i in range(n):   #n=5
#     for j in range(i):
#         print("*", end=" ")
#     print(" ")
#
# for i in range(n,0,-1):
#     for j in range(i):
#         print("*", end=" ")
#     print(" ")


# """5. Write a Python program that accepts a word from the user and reverses it."""
#
# word = input("Enter a word: ")
#
# # Reverse the word using slicing
# reversed_word = word[::-1]
#
# # Print the reversed word
# print("Reversed word:", reversed_word)

"""
# 6. Write a Python program to count the number of even and odd numbers in a series of numbers
# Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
# """
# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# even=[]
# odd=[]
# for num in numbers:
#     if num%2==0:
#         even.append(num)
#     else:
#         odd.append(num)
# print("Number of even numbers ", even)
# print("Number of odd numbers ", odd)

# """
# . Write a Python program that prints each item and its corresponding type from the following list.
# Sample List : datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
# """
# datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
#
# for i in datalist:
#     print(i, type(i))


# """
#  Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
# Note : Use 'continue' statement.
# """
#
# for i in range (0,7):
#     if i==3 or i==6:
#         continue
#     else:
#         print(i)

# """
# 9. Write a Python program to get the Fibonacci series between 0 and 50.
# Note : The Fibonacci Sequence is the series of numbers :
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# """
# x=0
# y=1
# while y<50:
#     print(y)
#     x,y=y,x+y


# """
# Write a Python program that iterates the integers from 1 to 50.
# For multiples of three print "Fizz" instead of the number
# and for multiples of five print "Buzz".
# For numbers that are multiples of three and five, print "FizzBuzz".
# """
#
# for i in range (1,51):
#     if i % 3==0  and i % 5==0:
#         print("FizzBuzz")
#     elif i % 3==0 :
#             print("Fizz")
#     elif i % 5==0:
#             print("Buzz")
#     print(i)


# """
# Write a Python program that accepts a string and calculates the number of digits and letters.
# Sample Data : Python 3.2
# Expected Output :
# Letters 6
# Digits 2
# """
#
# letter=0
# digit=0
# name=input("enter you string:- ")
# for i in name:
#         if i.isalpha():
#             letter=letter+1
#         elif i.isdigit():
#             digit=digit+1
# print(letter)
# print(digit)



# # Write a Python program to check the validity of passwords input by users.
# # Validation :
# #
# # At least 1 letter between [a-z] and 1 letter between [A-Z].
# # At least 1 number between [0-9].
# # At least 1 character from [$#@].
# # Minimum length 6 characters.
# # Maximum length 16 characters.
#
#
# def validate_password(password):
#     # Check length
#     if len(password) < 6 or len(password) > 16:
#         return "Password must be between 6 and 16 characters long."
#
#     # Initialize flags
#     has_lower = has_upper = has_digit = has_special = False
#
#     # Iterate over each character in the password
#     for char in password:
#         if char.islower():
#             has_lower = True
#         elif char.isupper():
#             has_upper = True
#         elif char.isdigit():
#             has_digit = True
#         elif char in "$#@":
#             has_special = True
#
#     # Check if all conditions are met
#     if not has_lower:
#         return "Password must contain at least one lowercase letter (a-z)."
#     if not has_upper:
#         return "Password must contain at least one uppercase letter (A-Z)."
#     if not has_digit:
#         return "Password must contain at least one digit (0-9)."
#     if not has_special:
#         return "Password must contain at least one special character ($, #, or @)."
#
#     return "Password is valid!"
#
# # Get password input from the user
# password = input("Enter your password: ")
# validation_message = validate_password(password)
# print(validation_message)


"""
# 16. Write a Python program to find numbers between 100 and 400 (both included) where each digit 
# of a number is an even number.The numbers obtained should be printed in a comma-separated sequence.
# """
# even=[]
# for i in range (100,401):
#     if i%2==0:
#         even.append(i)
#         # print(i,end=" , ")
# print(even)

# print("----------------------")
"""
*
**
***
****
*****
******
"""
# n=7
# for i in range(n):
#     for j in range(i):
#         print("*", end=" ")
#     print(" ")


# n=4
# for i in range(n):
#         print("*", end=" ")
#         print(" ")
# for j in range(n,1,-1):
#     print("*", end=" ")

# def pass_fail(score):
#     if score >=50:
#         result="passed"
#         return result
#     else:
#         result= "Failed"
#         return result
#
# re=pass_fail(40)
# print(re)


#
# # Print numbers until the user enters 0
# number = int(input('Enter a number: '))
#
# # iterate until the user enters 0
# while number != 0:
#     print(f'You entered {number}.')
#     number = int(input('Enter a number: '))
#
# print('The end.')