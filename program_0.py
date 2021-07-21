# write a script that prints the multiples of 7 between 0 and 100 pythonwrite a script that prints the multiples of 7 between 0 and 100 python		


def multiply(start,end):
    lst = []
    for i in range(start,end):
        if i%7 == 0:
            lst.append(i)
    print(lst)

a = multiply(0,100)                



