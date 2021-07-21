# 13). Please 
# write a program to output a random number, which is divisible by 5 and 7, between 0 and 10 inclusive using random module and list comprehension.


import random
my_list = [i for i in range(0,100) if i%5 == 0 or i%7 == 0]
output = random.sample(my_list,5)
print("Your List is:",output)