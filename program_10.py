# 10). Write a program which are divisible by 7 and between a given range 0 and n.
def div(start,end):
    
    for i in range(start,end):
        if i%7 == 0:
            print(i,end=',')

start = int(input("Start number"))
end = int(input("End number"))
a = div(start,end)