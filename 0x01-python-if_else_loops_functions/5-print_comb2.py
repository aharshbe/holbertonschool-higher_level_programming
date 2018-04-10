#!/usr/bin/python3
# for i in range(0, 100):
# 	if (i <= 9):
# 		i = str(0) + str(i)	
# 	if (not(i == 99)):
# 		print("{}, ".format(i), end='')
# 	else:
# 		print("{}".format(i))


for i in range(0, 100):
	if (i < 99):
		print("{:02d}, ".format(i), end='')
	else:
		print(i)
