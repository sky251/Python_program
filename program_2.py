# 2). Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320


def facto(num1):
    a = num1
    if num1 == 0 or num1 == 1:
        print("factorial of 0 and 1 is : 1 ")
    else:
        for i in range(1,num1):
            num1 = num1*i
        print("factorial of" ,a, "is:",num1)    


num1 = int(input("Enter a number:"))
a = facto(num1)    