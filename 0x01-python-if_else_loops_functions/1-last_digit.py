#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number < 0):
	x = abs(number)
else:
	x = number
if ((x % 10) > 5):
	print("Last digit of {} is {} and is greater than 5".format(number, x % 10))
elif (not (x % 10)):
	print("Last digit of {} is {} and is 0".format(number, x % 10))
elif ((x % 10) < 6 and (not 0)):
	print("Last digit of {} is {} and is less than 6 and not 0".format(number, x % 10))