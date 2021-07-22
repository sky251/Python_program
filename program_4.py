# 4). Write a program which accepts a sequence of comma-separated numbers from the console and generate a list and a tuple which contains every number. 
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')


def takeInput(numbs):
    lst = numbs.split(',')
    tup = tuple(lst)
    print(tup)

numbs = input('Enter numers: ')
a = takeInput(numbs)