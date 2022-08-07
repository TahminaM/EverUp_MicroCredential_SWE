"""
Python Exercises
Student's Name: Tahmina Munni
"""
 
import math
import random
 
# Activity: a
print("------------ ACTIVITY 3a ------------")
 
fruitArray = []
size = int(input("Enter the number of fruits: "))
count = 0
for i in range(1,size+1):
   count += 1
   item = input(("Fruit " + str(count)+ ": "))
   fruitArray.append(item)
print("User created a list of " + str(size) + " items and entered the values: ", fruitArray)
 
 
 
 
# Activity: b
print("-------------Exercise 3: Print between a specific range-----------\n")
 
# Storing the range
num1=int(input("Enter number 1: "))
num2=int(input("Enter number 2: "))
 
# If both the entered values are same
while num1 == num2:
   num2 = int(input("Enter a different number: "))
 
# Printing the values between a specified range
if num1 < num2:
   for i in range(num1, num2):
       print(i)
else:
   for i in range(num2, num1):
       print(i)
 
 
 
 
# Activity: c
print("--------- Activity C --------- ")
radius = int(input("Enter a radius: "))
height = int(input("Enter a height: "))
 
def volumeCylinder(h,r):
   volumeC = r**2*math.pi*h
   return round(volumeC, 2)
 
volumeCylinder(radius, height)
print("The volume with radius %s and height %s is %s" %(radius, height, volumeCylinder(height, radius)))
 
 
 
 
# Activity: d
print("--------- Activity D --------- ")
numRoll = int(input("How many times do you want to roll? "))
    
def rollDice(numRoll):
   for i in range(1, numRoll+1):
       randomNumber = random.randint(1,6)
       print("Roll %s = %s" %(i,randomNumber))
      
rollDice(numRoll)
       
 
 
 

