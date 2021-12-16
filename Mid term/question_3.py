# Question 3

# Write a python program that reads two integer numbers from the keyboard and 
# shows on the console the greatest common divisor (gcd) of them.

#Note: The function gcd is defined in the module math.

import math 

integer_1 = int(input("Please Enter the interger 1: \n"))

integer_2 = int(input("Please Enter the interger 2: \n"))

gcd = math.gcd(integer_1,integer_2)

print(f"The greatest common divisor (gcd) of {integer_1} and {integer_2} is {gcd}.")