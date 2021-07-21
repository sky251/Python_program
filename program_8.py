# 8). Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# D means deposit while W means withdrawal.
# Then, the output should be:
# 500

import sys

fd=0
fw=0
str=sys.stdin.readlines()
for s in str:
	if s[0]=="D":
		temp=s.split(" ")
		fd+=int(temp[1])
	elif s[0]=="W":
		temp=s.split(" ")
		fw+=int(temp[1])
print("balance is: ",fd-fw)