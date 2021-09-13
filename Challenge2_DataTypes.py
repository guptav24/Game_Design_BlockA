#Vivaan Gupta
#09/13/2021
import os
os.system('cls')

#This is about data types and how strings work
userInput = input("Type something: ")
try:    #Trial and error function
    int(userInput)
    check = True
except ValueError:
    check = False

if (check):
    print()
else:
    print(len(userInput))   #Prints the length of the input in characters

for i in userInput:
    print (i)

if len(userInput > 3):
    print (userInput[3])
