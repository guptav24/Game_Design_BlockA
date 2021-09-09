#Vivaan Gupta
#09/09/2021
#Arithmetic Operators
#+ - * / % (% is a mod - remainder)

#Import library
import os
os.system('cls')

#Ask User for number
num = int(input("What number do you want to check? "))
rem = num%2
remPlace1 = num%10
remPlace2 = num%100
remPlace3 = num%1000

# #Conditional
# if(rem == 0):
#     print ("It is even")
# else:
#     print ("It is odd")

if(num<10):
    print("The first number is ", remPlace1)
elif (num<100):
    print("The first number is ", remPlace1)
    print("The last 2 numbers are ", remPlace2)
else:
    print("The first number is ", remPlace1)
    print("The last 2 numbers are ", remPlace2)
    print("The last 3 numbers are ", remPlace3)