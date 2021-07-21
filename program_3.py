# 3). With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary. 
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

def dicti(l,n):
    dic = dict()
    for num in range(l,n+1):
        dic[num] = num*num
    print(dic)

l = int(input("Staring number:"))        
n = int(input("Ending number:"))

a = dicti(l,n)




