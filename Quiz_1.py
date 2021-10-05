#Vivaan Gupta
#10/5/2021
#This is the code for quiz 1

import os
os.system('cls')

print(len('Hello World!'))  #1

strString = "Study.com is a wonderful resource."    #2
print(strString.find("great"))  #2
print(strString.find("wonderful"))  #2
print(strString.find("."))  #2

print(strString[15:24]) #3

print(strString[0]) #0 is the index for the first character, this should print out "S"  #4

print(strString[15:24].find("der")+len(strString))  #5

var1 = 17   #6
var2 = 4    #6
result = var1%var2  #6
print (result)  #6

str = "Hello. I am taking my quiz today.\tIt is October 5th"    #7
print (str) #7

str2 = "Hello. I am taking my quiz today.\nIt is October 5th"    #8
print (str2) #8

print("My name is " + "Vivaan") #9

MyList = ["0","1","2","3","4","6","7","8","9","10"] #10
MyList.insert(5, "5")  #10
print (MyList)  #10