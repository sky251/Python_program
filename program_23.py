# 23). By using list comprehension, please write a program to print the list after removing the value 24 in the list [12,24,35,70,88,120,155].

lst = [12,24,35,70,88,120,155]
lst = [x for x in lst if x != (24,35)]
print(lst)

