# 6). Write a program that accepts a sentence and calculate the number of uppercase letters and lowercase letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

def Cnt(sent):
    upper = 0
    lower = 0
    for ch in sent:
        if ch.islower():
            lower = lower + 1
        else:
            upper = upper + 1    
    print("Lower CASE: ",lower)        
    print("UPPER CASE: ",upper)

sent = input("Enter your sentence:")
a = Cnt(sent)    
