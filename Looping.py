#Vivaan Gupta
#09/07/2021
#We are going to learn how to use a for loop

#Import Library
import os

#Use library to clear terminal
os.system('cls')

#Input number of stars
stars = int(input("How many stars do you want? "))
line=stars
space = 0   #Start number of spaces

# for i in range(line):
#     for counter in range(stars):
#         print("*", end=" ")
#     print()
#     stars = stars-1

# for line in range(stars):
#     for space in range(stars):
#         spaceText = "  "*space    #Turn the number of spaces into text
#         print(spaceText, end="")  #Print the spaces
#         space = space+1   #Increase number of spaces needed by 1
#         for counter in range(stars):
#             print("*", end=" ")   #Print number of stars
#         print()
#         stars=stars-1     #Decrease number of stars by 1

for line in range(stars):
    for counter in range(stars):    #Print stars
        print("*", end="")
    spaceText = " "*space
    print (spaceText, end="")   #Print number of spaces needed
    for counter in range(stars):
        print("*", end="")  #Print stars again
    print()
    space += 2  #Increase spaces by 2, shortcut for space = space + 2
    stars -= 1  #Decrease stars by 1, shortcut for stars = stars - 1

#Ending
print("Thank you!") 