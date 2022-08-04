# Tahmina A Munni: Activity 17


print("Hello World from Python!")

# creating variables
number1 = -30
number2 = 15.6
addiition = number1 + number2
name = "Tahmina Munni"
character = 'T'


# Boolean for later
no_yes = False
print("Number 1 = ", number1)


# Input() Function
firstName = input("Enter a name: ")
print("Welcome to the program: ", firstName)


# casting from string to integer
num1 = input("Enter a number: ")
num1 = int(num1)
num2 = int(input("Enter a 2nd number: "))
prod = num1*num2
print("The product of ", num1, " and ", num2, " is ", prod)


#ex 1: find the hypotenuse of a right angle
h = float(input("Enter the height: "))
w = float(input("Enter the width: "))
hyp = (h**2+w**2)**0.5
print("A hypotenuse is: ", hyp)


#strings
msg = input("Enter a message: ")
fullName = input("Enter a full name: ")
print("%s. Welcome %s" %(msg, fullName))
nameLen = len(fullName)
lastCharName = fullName[nameLen - 1]
index_a = fullName.find("a")
print("Name %s has %s characters and the last character is: %s " %(fullName.upper(), nameLen, lastCharName))
print("Name %s has letter a with index %s " %(fullName, index_a))


#lists
fruits = ["apples", "oranges", "grapes", "pears", "cherries", "mangos"]
print(fruits)
copyFruits = fruits.copy()
copyFruits.reverse()
copyFruits.append("berrries")
print("Original list %s \n Copy list %s" %(fruits, copyFruits))
numGrapes = copyFruits.count("grapes")
numKiwi = copyFruits.count("kiwis")
indexPears = fruits.index("pears")
print("There are ", numGrapes, "grapes in the list")
print("There are ", numKiwi, "kiwis in the list")
print("Pears has index", indexPears)


"""
Multiple Line
........
........
Comments
"""