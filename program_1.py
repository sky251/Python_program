# 1). Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.

def multiply(start,end):
    lst = [i for i in range(start,end) if i%7 == 0 and i%5 != 0]

start = int(input("Start number:"))
end = int(input("End number :"))
a = multiply(start,end)                
