#Vivaan Gupta
#09/27/2021
#This program is a guessing game

import os
import random 

os.system('cls')
counter = 1
program = 1
words = ["peach","apple","orange","grape","cherry","watermelon","banana","strawberry","blueberry","mango"]
print ("This is a list of fruits. I have chosen a random fruit from this list. You have 5 guesses to try and guess which fruit I chose!")
game = input("Do you want to play? Type Y for yes or N for no: ")
randWord = random.choice(words)   #This picks a random word in the list
print(randWord)

while ("Y" and "y" in game):

    while (program == 1 and counter<6):

        guess = input("Give me a fruit: ")
        guess = guess.lower()
        turns = 5 - counter    #This is how many turns you have left
        if(guess == randWord):   #If you got it right
            print("You win!")
            print("You took",counter,"tries!")
            program=0

        else:
            print(turns, "turns left")
            print("Try again")

        counter +=1

    if (counter == 6):        
        print("You lost!")
        print("You used all your tries!")
        program = 0

    game = input("Do you want to play again? Type Y for yes or N for no: ")
    if "y" or "Y" in game:
        program = 1
        counter = 1
    else:
        game = 'N'

print ("Thank you for playing!")
