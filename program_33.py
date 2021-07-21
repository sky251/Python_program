# 33).  Write a program to generate below Pattern:


# 		* * * * * *
# 		 * * * * *
# 		  * * * *
# 		   * * *
# 		    * *
# 		     *



x = int(input("Enter number of raw: "))
for i in range(0,x):
    for j in range(0,i+1):
        print(' ',end='')

    for s in range(i,x):
        print('* ',end='')

    print()        