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



