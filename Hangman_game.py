#Vivaan Gupta
#09/27/2021
#This is a hangman game

from hashlib import new
import os
import random 
os.system('cls')

words = ["peach","apple","orange","grape","cherry","watermelon","banana","strawberry","blueberry","mango"]
print(" ".join(words))
print ("This is a list of fruits. I have chosen a random fruit. You have to guess a random letter and try to spell out the word.")
name = input("What is your name? ")
game = input(name + ", do you want to play? Type Y for yes or N for no: ")
counter = 0
wins = 0

while ("Y" and "y" in game):  #If you want to play
    print("Good Luck "+name+"! You have 5 lives")
    turns = 5
    counter += 1
    randWord = random.choice(words)
    randWord = randWord.lower()
    print(randWord)
    guesses = " "
    for letter in randWord:
        if letter in guesses:
            print (letter,end=" ")
        else:
            print("_",end=" ")
    while turns > 0:
        print()
        newGuess = input("Guess a letter: ")
        newguess = newGuess.lower()
        if newGuess in randWord:
            guesses+=newGuess
            print("You guessed a correct letter!")
        else:
            turns -= 1
            print("That is not in the word. You have ", turns, " lives left")
        for letter in randWord:
            if letter in guesses:
                print (letter,end=" ")
            else:
                print("_",end=" ")
                
    game = input("Do you want to play again? Type Y for yes or N for no: ")

print("Thank you for playing!")
        
    


