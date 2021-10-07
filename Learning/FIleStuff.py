#Vivaan Gupta
#10/07/2021
#We are going to learn how to:
#Open() a file
#Write to a file
#Read from a file
#Append to a gile
#Close() a file

import os, time
os.system('cls')

#To create a file you must declare an object so we can open a file
#When you open a file for the first time you need to use 'w
myFile = open('score.txt','w')
myFile.write("Hello there, my name is Vivaan \t What is yours?")
myFile.close()
#Always close a file when you are done using it
fileMy = open('score.txt','r')
print(fileMy.read())
fileMy.close()
score = 450
anotherFile = open('score.txt','a')
anotherFile.write("The highest score: \t"+str(score))
anotherFile.close()