# Vivaan Gupta
# 09/02/2021
#This program will calculate the average of 4 test scores

#These are my variables
test1 = 90
test2 = 87
test3 = 89
test4 = 93

#Declare sum and average
sum = (test1 + test2 + test3 + test4)
average = sum/4

#Display Average
print("The average is ",average)

#New test score
test5 = int(input("What is the test 5 score? "))
sum = sum+test5
average = sum/5

#Display new average 
print("The new average is ",average)
