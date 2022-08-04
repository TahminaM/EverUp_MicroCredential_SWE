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