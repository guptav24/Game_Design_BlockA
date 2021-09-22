#Vivaan Gupta
#09/21/2021
#This program is a guessing game

import os
import random 

os.system('cls')

game = "Y"
print ("I have picked a number between 1 and 100. You have to guess. You have 10 guesses. I will give you a hint each time.")

while game == "Y":
    randNum = random.randrange(1,100)   #This picks a random number btween 1-100
    for counter in range(1,11): #This starts a loop with 10 guesses
        guess = input("Give me a number: ")
        turns = 10 - counter    #This is how many turns you have left
        try:
            guess = int(guess)  #Tries if it is an integer
        except ValueError:
            print("You lose a turn because you did not give a valid number")
            print("You have ", turns, " left")
            continue

        if (guess > 100 or guess < 0):  #Checks if the guess is between 1-100
            print("You lose a turn because you did not give a valid number")
            print("You have ", turns, " turns left")

        else:
            if(guess == randNum):   #If you got it right
                print("You win!")

                else:
                    print("Thank you for playing!")
            else:
                print("Try again")
                if (guess < randNum):
                    print("Your number is too low")
                    print("You have ", turns, " left")

                else:
                    print("Your number is too high")
                    print("You have ", turns, " left")
        if (counter == 10): #If you used up all your tries
            print("You lost!")
