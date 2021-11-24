#Basic Statistics Calculator (considering the numpy package)
# Md Salman Rahman


import os
import sys
import math
import numpy as np

# Series initialization
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
	min = np.min(x)		
	print("\nMinimum: ", min, end='')


def showMaximum(x):
	max = np.max(x)
	print("\nMaximum: ", max, end='')


def showSum(x):
	sum = np.sum(x)
	print("\nSum: ", sum, end='')


def showMean(x):
	mean = np.mean(x)
	print("\nMean: ", mean, end='')


def sum(x):
	sum = np.sum(x)
	return(sum)


def showSD(x):
	variance = np.var(x)
	sd = np.std(x)
	print("\nVariance:", f"{variance:.2f}")
	print("Standard Deviation:",f"{sd:.2f}", end='')

def showFullReport(x):
	showSeries(x)
	showMinimum(x)
	showMaximum(x)
	showSum(x)
	showMean(x)
	showSD(x)
					
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
		else:
			break

#Entry point of the program
main()
		







