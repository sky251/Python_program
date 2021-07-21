# 16). Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7 , between 1 and 1000 inclusive.

def div(start,end):
    lst = []
    for i in range(start,end):
        if i%7 == 0 and i%5 ==0:
            lst.append(i)
    print(lst[:5])        

start = int(input("Start number:"))
end = int(input("End number:"))
a = div(start,end)