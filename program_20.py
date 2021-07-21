# 20). By using list comprehension, please write a program to print the list after removing delete numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].


lis = [12,24,35,70,88,120,155]
x = [var for var in lis if var%7!=0 and var%5!=0 ]
print(x)