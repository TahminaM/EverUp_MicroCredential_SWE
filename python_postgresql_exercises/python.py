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














import math
import random
print("--------- Activity A --------- ")
fruitList = []

numFruits = int(input("Enter the number of fruits: "))
for i in range(1, numFruits + 1):
    fruitVal = input("Fruit %s: " %(i))
    fruitList.append(fruitVal)
print("User created a list of %s items and entered the values: %s" %(numFruits, fruitList))

print("--------- Activity B --------- ")
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: " ))

while num1 == num2:
    num2 = int(input("Enter a different number: "))

if num1 < num2:
    for i in range(num1, num2):
        print(i)
else:
    for i in range(num2, num1):
        print(i)

print("--------- Activity C --------- ")
radius = int(input("Enter a radius: "))
height = int(input("Enter a height: "))

def volumeCylinder(h,r):
    volumeC = r**2*math.pi*h
    return round(volumeC, 2)

volumeCylinder(radius, height)
print("The volume with radius %s and height %s is %s" %(radius, height, volumeCylinder(height, radius)))


print("--------- Activity D --------- ")
numRoll = int(input("How many times do you want to roll? "))
      
def rollDice(numRoll):
    for i in range(1, numRoll+1):
        randomNumber = random.randint(1,6)
        print("Roll %s = %s" %(i,randomNumber))
        
rollDice(numRoll)
         


