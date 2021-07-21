# 14). Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.

import random
my_list = [i for i in range(100,200)]
output = random.sample(my_list,5)
print("Your List is:",output)