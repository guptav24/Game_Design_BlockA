#Vivaan Gupta
#09/27/2021
#This is a word guessing game

import os
import random 
os.system('cls')

def updateWord(randWord,guesses):   #Print the dashes and letters (like _ _ a _ _ ) function
    for letter in randWord:
        if letter in guesses:
            print (letter,end=" ")
        else:
            print("_",end=" ")

def printScores():  #Function to print socres
    myFile=open('score.txt','r')
    print(myFile.read())
    myFile.close()

def updateScores(): #Funvtion to update scores
    myFile=open('score.txt','w')
    myFile.write('High Score: '+name+': '+str(maxScore))
    myFile.close()

def menu(): #Menu
    print("____________________________________________________")
    print("|                                                  |")
    print("|    This is a guessing game! Choose a category!   |")
    print("|                                                  |")
    print("|                       MENU                       |")
    print("|                                                  |")
    print("|                   1. ANIMALS                     |")
    print("|                   2. FRUITS                      |")
    print("|                   3. COMP PARTS                  |")
    print("|                   4. SCOREBOARD                  |")
    print("|                   5. EXIT                        |")
    print("|                                                  |")
    print("| To play the game, select 1-4, to exit, select 5. |")
    print("|                                                  |")
    print("____________________________________________________")
    print()
    sel=input("What would you like to do? ")
    if sel == 4:    #Prints the scores if 4 is chosen
        printScores()
    if sel == 5:    #Updates scores when exited
        randWord = ""
        updateScores()
    try:
        sel = int(sel)  #Tries if it is an integer
        if sel < 6 and sel > 0:
            check = True
            return sel
    except ValueError:
        print("Give me a number from 1 - 4. Try Again")
        sel=input("What would you like to play? ")
        check = False
        
def selWord(sel):   #Function to choose a random word from the different lists
    if sel == 1:
        randWord = random.choice(animals)
    if sel == 2:
        randWord = random.choice(fruits)
    if sel == 3:
        randWord = random.choice(compParts)
    if sel == 4:
        printScores()
        randWord = ""
    if sel == 5:
        randWord = ""
        updateScores()
    return randWord

animals = ["tiger","elephant","monkey","lion","zebra","panther","rhino","dog","cat","bird","fish"]
compParts = ["keyboard","monitor","computer","case","trackpad","headphone","motherboard","microphone"]
fruits = ["peach","apple","orange","grape","cherry","watermelon","banana","strawberry","blueberry","mango"]

name = input("What is your name? ")
maxScore = 0
game = "y"
sel=menu()  #Menu function
if sel == 4:
    randWord = ""
    printScores()
    sel = menu()
while (sel==1 or sel == 2 or sel == 3) and ("Y" and "y" in game):   #Y/y for play again
    randWord = selWord(sel)
    randWord = randWord.lower()
    wordCount = len(randWord)
    turns = len(randWord) + 3   #Number of tries you have
    print("Good Luck ",name,"! You have ", turns," lives")
    guesses = ""
    updateWord(randWord,guesses)
    letCount = 0

    while turns > 0 and letCount<wordCount: #letCount increases by 1 each time you get a correct letter, and when it is equal to the number of letters in randWord, you win
        letCount = 0
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
                letCount+=1
            else:
                print("_",end=" ")

    if turns == 0:
        print("You lose!")
    else:
        print()
        print("You win!")
    score = 3*wordCount+5*turns #Score calculator
    if score>maxScore:  #Checks high score
        maxScore = score
    myFile=open('score.txt','w')
    myFile.write('High Score: '+name+': '+str(maxScore))    #Writes the score down
    myFile.write("\n")
    myFile.write(name+": "+ str(score))
    myFile.close()
    game = input("Do you want to play again? Type Y for yes or N for no: ") #Play again
    if ("Y" and "y" in game):
        os.system('cls')
        sel = menu()
        if sel == 4:
            randWord = ""
            printScores()
            sel = menu()
    if ("n" and "N" in game):
        sel = 5
        updateScores()

print("Thank you for playing!")
updateScores()
