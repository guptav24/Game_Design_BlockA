#using random numbers
#guess a number

import os
import random 

os.system('cls')

# random.seed(20)
# for i in range(10):
#     randy = random.randint(3,5)
#     print(randy)
#     randy2 = random.randint()
#     randy2 *= 100
#     print(int(randy2))

fruits=["apple", "banana", "berries"]
myFruit= random.choice(fruits)
print(myFruit)