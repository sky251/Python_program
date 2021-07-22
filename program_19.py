# 19). Please write a program to print the list after removing even numbers in [5,6,77,45,22,12,24].


lst = [5,6,77,45,22,12,24]

lst = [num for num in lst if num%2 != 0]
print(lst)        
