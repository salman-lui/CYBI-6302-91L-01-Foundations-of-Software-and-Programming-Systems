# Question 4
'''
Complete functionality 9 of the menu-driven program that shows on the console statistic values from a series of n 

integers numbers inserted by the user (template Lab_3.3). 
The length of the series must be defined by the user and the random integer values generated must be in the in the interval [1-6].
 
BASIC STATISTICS CALCULATOR:
1.- Insert Series
2.- Minimum
3.- Maximum
4.- Sum
5.- Arithmetic Mean
6.- Standard Deviation
7.- Full Report
8.- Show Series
9.- Generate random series (1-6)
 
0.- Quit

'''

import os
import sys
import math
import random
# Series initializationthere i
x = []       
x.append(0);

# Detect the host system
if sys.platform.startswith('win'): 
	CLEAN = "cls"
else:
	CLEAN = "clear"	


def menu():
	option = 0
	print("\n\nBasic Statistics Calculator\n")
	print(" 1. Insert series")
	print(" 2. Minimum")
	print(" 3. Maximum")
	print(" 4. Sum")
	print(" 5. Show mean")
	print(" 6. Variance and Standard Deviation")
	print(" 7. Full Report")
	print(" 8. Show series")
	print(" 9. Generate random series (1-6)")
	print("\n 0. Quit\n")

	option = int(input("Insert option: "))
	return(option);


def dataInput():
	global x
        #Let's empty array x = [] or
	for k in range(len(x)):
		x.pop()

	num = int(input("Insert number of elements: "))
	#Let's fill array
	for k in range(num):
		x.append(int(input(f"\nInsert x{k}:")))


def showSeries(x):
	print(f'\nSeries: {x}')
	print('Series length:', len(x), end='')



def showMinimum(x):
	min = x[0]
	for k in range(len(x)):
		if (x[k]<min):
			min=x[k]		
	print("\nMinimum: ", min, end='')


def showMaximum(x):
	max = x[0]
	for k in range(len(x)):
		if (x[k]>max):
			max=x[k]
	print("\nMaximum: ", max, end='')


def showSum(x):
	sum = 0
	for k in range(len(x)):
		sum+=x[k]
	print("\nSum: ", sum, end='')


def showMean(x):
	sum = 0
	for k in range(len(x)):
		sum+=x[k]
	print("\nMean: ", sum/len(x), end='')


def sum(x):
	sum = 0
	for k in range(len(x)):
		sum+=x[k]
	return(sum)

def showSD(x):
	mean = sum(x)/len(x)
	variance = 0;
	for i in range(len(x)-1):
		variance=variance+math.pow((mean-x[i]),2)
	variance = variance/len(x)
	print("\nVariance & Standard Deviation:", f"{variance:.2f}",
              " &  ",f"{math.sqrt(variance):.2f}", end='')



def showFullReport(x):
	showSeries(x)
	showMinimum(x)
	showMaximum(x)
	showSum(x)
	showMean(x)
	showSD(x)


def generateRandomNumber(x):
	series_length = int(input("Length of the series inserted by the user: "))
	for i in range(1,series_length):
		number = random.randint(1,6)
		x.append(number)
	print(x)


def main():
	op = 0
	while (True):
		op = menu()
		os.system(CLEAN)

		if (op == 1):
			dataInput()
		elif (op == 2):
			showMinimum(x)
		elif (op == 3):
			showMaximum(x)
		elif (op == 4):
			showSum(x)
		elif (op == 5):
			showMean(x)
		elif (op == 6):
			showSD(x)
		elif (op == 7):
			showFullReport(x)
		elif (op == 8):
			showSeries(x)
		elif (op == 9):
			generateRandomNumber(x)
		else:
			break

#Entry point
if __name__ == '__main__':
	main()
		







