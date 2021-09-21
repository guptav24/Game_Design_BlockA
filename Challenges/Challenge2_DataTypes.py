#Vivaan Gupta
#09/13/2021
import os
os.system('cls')

# #This is about data types and how strings work
# userInput = input("Type something: ")
# try:    #Trial and error function
#     int(userInput)
#     check = True
# except ValueError:
#     check = False

# if (check):
#     print()
# else:
#     print(len(userInput))   #Prints the length of the input in characters

# for i in userInput:
#     print (i)

# if len(userInput > 3):
#     print (userInput[3])

var1 = "Hello World"
var2 = 10
var3 = 5.4
var4 = True
print (var1, " Is a data type of ", type(var1))
print (var2, " Is a data type of ", type(var2))
print (var3, " Is a data type of ", type(var3))
print (var4, " Is a data type of ", type(var4))

num1 = 100
num2 = 20
sum = num1 + num2
div = num1/num2
mult = num1*num2
sub = num1 - num2
mod = num1%num2
print(num1, " plus ", num2, " is ", sum)
print(num1, " minus ", num2, " is ", sub)
print(num1, " multiplied by ", num2, " is ", mult)
print(num1, " divided by ", num2, " is ", div)
print("The remainder of ", num1, " divided by ", num2, " is ", mod)