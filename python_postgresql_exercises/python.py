"""
Python and Postgresql Exercises
Student's Name: Tahmina Munni
"""

import math 
import random

# a





# b

print("-------------Exercise 3: Print between a specific range-----------\n")
# Storing the range
a=int(input("Enter number 1: "))
b=int(input("Enter number 2: "))

# If both the entered values are same
while a==b:
    b = int(input("Enter another number for the last number:"))

# Printing the values between a specified range
while a<b:
    print(a)
    a+=1