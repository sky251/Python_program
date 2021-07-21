# 15). Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.

import random
my_list = [i for i in range(100,200) if i%2 == 0]
output = random.sample(my_list,5)
print("Your List is:",output)