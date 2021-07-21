# 7). Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106


def addd(num):
    n1= num*1
    n2 = num*2
    n3 = num*3
    n4 = num*4
    total = int(n1) + int(n2)+ int(n3)+ int(n4)
    print(total)

num = str(9)
a= addd(num)