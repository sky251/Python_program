# 30).  Write a program to generate below Pattern:

# 	*
# 	* *
#  	* * *
# 	* * * *
# 	* * * * *
# 	* * * * * *

x = int(input("Enter number of raw: "))
for i in range(0,x+1):
    print('*'*(x-i))