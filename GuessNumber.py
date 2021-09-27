#Vivaan Gupta
#09/21/2021
#This program is a guessing game

import os
import random 

os.system('cls')
counter = 1
program = 1
print ("I have picked a number between 1 and 100. You have to guess. You have 10 guesses. I will give you a hint each time.")
game = input("Do you want to play? Type Y for yes or N for no: ")
randNum = random.randrange(1,100)   #This picks a random number btween 1-100

while ("Y" and 'y' in game):

    while (program == 1 and counter!=11):

        guess = input("Give me a number: ")
        turns = 10 - counter    #This is how many turns you have left

        try:
            guess = int(guess)  #Tries if it is an integer
        except ValueError:
            print("You lose a turn because you did not give a valid number")
            print(turns, " turns left")
            continue

        if (guess > 100 or guess < 0):  #Checks if the guess is between 1-100
            print("You lose a turn because you did not give a valid number")
            print(turns, " turns left")

        else:
            if(guess == randNum):   #If you got it right
                print("You win!")
                print("You took",counter,"tries!")
                program=0

            else:
                counter +=1
                print("Try again")
                if (guess < randNum):
                    print("low")
                    print(turns, " turns left")

                else:
                    print("high")
                    print(turns, " turns left")

        if (counter == 10): #If you used up all your tries
            print("You lost!")
            print("You took",counter,"tries!")
            program = 0

    game = input("Do you want to play again? Type Y for yes or N for no: ")
    if "y" or "Y" in game:
        program = 1
        counter = 1
    else:
        game = 'N'
