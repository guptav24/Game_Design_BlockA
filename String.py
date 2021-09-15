#Vivaan Gupta
#09/15/2021
#This program is about strings

import os
os.system('cls')

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.") #Checks if a word is in a string

b = "Hello, World!"
print(b[-5:-2]) #Will pring out "orl" (Negative makes it go back to front in the place number)

a = "Hello, World!"
print(a.split(",")) #Will print ['Hello', ' World!']

a = "Hello"
b = "World"
c = a + " " + b
print(c)    #Prints 'Hello World"

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))  #Prints the variable where the brackets are in that order

txt = "We are the so-called \"Vikings\" from the north."    #Let's you put quotations in quotations
