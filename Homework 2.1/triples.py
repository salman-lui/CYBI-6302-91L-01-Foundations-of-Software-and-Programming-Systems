#Author: Md Salman Rahman
'''
Write a computer program in Python that uses nested loops to generate all of the primitive Pythagorean triples from 1 up to a provided number. 
The program will show the list of primitive Pythagorean triples as well as the total number of triples. 
For three integer numbers to be a primitive Pythagorean triple, they have to satisfy several requirements. 
First, the three numbers in the triple must satisfy the Pythagorean relationship a^2 + b^2 = c^2. 
Second, the three numbers fulfill the relationships of order  b > a  and c > b. 
Lastly, the greatest common factor of a, b, and, c must be no greater than 1. 
'''

import math
provided_number = 100
count=0
for a in range(1,provided_number):
    for b in range(1,provided_number):
        for c in range(1,provided_number):
            if((c**2==a**2+b**2) and (b>a and c>b)):
                if math.gcd(a,b,c)==1:
                    print(a,b,c)
                    count+=1



print(count) # additional things to see the count 



