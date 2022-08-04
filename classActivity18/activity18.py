# Name : Tahmina A Munni
# Activity : 18


#ex 1: if statement + if else statement - check if an age is an adult
print("\n\n------------------ CONDITIONAL STATEMENT ------------------")
age = int(input("Enter an age: "))
if age >= 21:
    print("You are an adult")
else:
    print("You are underage")
print("Welcome to the class")



#ex 2: if, elif and else statament
age = int(input("Enter an age: "))
if age == 5:
    print("Age = 5. Height should be around 102cm and weigth 14.8lbs")
elif age == 6:
    print("Age = 6. Height should be around 108cm and weigth 16.3lbs")
elif age == 7:
    print("Age = 7. Height should be around 113cm and weigth 18.0lbs")
else:
    print("Unable to display height and weigth")



#ex 3: and + or operators
age = int(input("Enter an age: "))
gender = input("Type M for male or F for female: ")
if age == 5 and gender == "M" or gender == "m":
    print("5 year old boy")
elif age == 5 and gender == "F" or gender == "f":
    print("5 year old girl!")
else:
    print("Any other ages other than 5")



# For loop:  ex 4: for loop basics   
print("\n\n------------------ FOR LOOP ------------------")
for x in range(1,5):
    print("Counting: ", x)



#Example 5: For loop with three arguments"
print("Example 5: For loop with three arguments")
for y in range(2, 30, 3):
    print("y = ", y)



#ex 6: for loop decrement count
for z in range(20,-10,-5):
    print("z =  ", z)



#ex 7: for loop in a list
print("Example 7: For loop in a list")
colors = ['yellow', 'red', 'blue', 'green', 'white', 'black']
for c in colors:
    print("color = ", c)



#ex 8: for loop in a string
msg = "Hello World"
for m in msg:
    print("characters = ", m)   


    
#Example 9: Nesting for loop and if statement
for counter in range(10):
    if counter == 5:
        continue #break
    print("Now counting: ", counter)
    print(" =*=*=*=*=*=*=*=*=*=*=*=*")



#ex 10: for loop to print num from 10 to -5 and skip nums that are multiple of 4
for num in range(10, -5, -1):
    if num%4 == 0:
        continue
    print(num)



#ex 11: for else statement
for n in range(7):
    print(n)
else:
    print("Done!!")



#ex 12: while loop basics
print("\n\n------------------ While LOOP ------------------")
i = 0
while i < 6:
    print("i = ", i)
    i += 1
else:
    print("i is no longer less than 6")



#ex 13: while loop to increment each num by 2 until it reaches up to 20
print("User enters two numbers between 0 and 10. Use while loop to increment each number by 2 until both of them reach up to 20")

num1 = int(input("Enter a number between 0 and 10: "))  
num2 = int(input("Enter a number between 0 and 10: "))

while num1 <= 20 and num2 <= 20:
    print("number 1 = %s and number 2 = %s" %(num1, num2))
    num1 += 2
    num2 += 2



#ex 14: create a while loop that checks if an entered number is between 0 and 10
print("Checkpoint: Create a while loop that checks if an entered number is between 0 and 10")

number = int(input("Enter a number between 0 and 10: "))
while number < 0 or number > 10:
    number = int(input("Try again! Enter a number between 0 and 10: "))
print("Entered number = ", number)



#ex 15: ask user to enter 2 nums between 0 and 10 w/ checkpoint. Use a while loop to incremenet each num by 2 until the sum of them reach up to 30
print("Ask user to enter two numbers between 0 and 10 with checkpoints. Use a while loop to increment each number by 2 until the sum of them reach up to 30")

number1 = int(input("Enter a number between 0 and 10: "))
while number1 < 0 or number1 > 10:
    number = int(input("Try again! Enter a number between 0 and 10: "))


number2 = int(input("Enter a number between 0 and 10: "))
while number2 < 0 or number2 > 10:
    number = int(input("Try again! Enter a number between 0 and 10: "))

while number1 <= 20 and number2 <= 20:
    addition = number1 + number2
    if addition > 30:
        break
    print("%s + %s = %s" %(number1, number2, addition))
    number1 += 2
    number2 += 2