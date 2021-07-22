# 7). Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106



def addd(num, digit):
    result = 0
    for i in range(1,num+1):
        result = result + int(str(digit*i))
    print(result)


digit = input("Enter digit:")
a= addd(4,digit)