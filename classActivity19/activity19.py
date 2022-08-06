# Name: Tahmina A Munni
# Activity : 19


import math
import random


# example 8: pass statement
def filter_num():
    pass


# example 7: Boolean functions
def is_divisible(x, y):
    print("----- EXAMPLE 7 -----")
    if x % y == 0 or y % x == 0:
        return True
    else:
        return False


# example 6: def function with parameters and return value
def sum(num1, num2):
    return num1 + num2

def number():
    print("----- EXAMPLE 6 -----")
    n1 = int(input("Enter number 1: "))
    n2 = int(input("Enter number 2: "))
    x = sum(n1, n2)
    print("The sum of %s and %s is %s" %(n1, n2, x))



# example 5: defined function with default parameter and no return value
def country(c="Norway"):
    print("----- EXAMPLE 5 -----")
    print("I am from", c)



# example 4: defined function with parameter and no return value
def name(fname):
    print("----- EXAMPLE 4 -----")
    print("Welcome to the program:", fname)



# example 3: defined function: no parameter no return value
def my_function():
    print("----- EXAMPLE 3 -----")
    print("Hello from function!\n")



# example 2: random numbers. Randomly pick a color from a list
print("----- EXAMPLE 2 -----")
colors = ["red", "blue", "green"]
randomIndex = random.randint(0, 2)
print("The picked color is:", colors[randomIndex])



# example 1: using built-in fiunction math to calculate the
# circumference given the radius
print("----- EXAMPLE 1 -----")
radius = int(input("Enter a radius: "))
circumference = round(2 * math.pi * radius, 2)
area = math.pow(radius, 2) * math.pi
print("The circumference with radius %s is %s" %(radius, circumference))
