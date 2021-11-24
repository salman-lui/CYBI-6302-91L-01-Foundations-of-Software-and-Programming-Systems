#Basic Statistic Calculator based on menu
# Md Salman Rahman

import os
import math
import sys
import numpy as np

x = []
x.append(0);

# Detect the host system
if sys.platform.startswith('win'): 
	CLEAN = "cls"
else:
	CLEAN = "clear"	
	

def menu():
	option = 0
	print("\n\nBasic Calculator\n")
	print(" 1. Insert series")
	print(" 2. Minimum")
	print(" 3. Maximum")
	print(" 4. Sum")
	print(" 5. Show mean")
	print(" 6. Variance and Standard Deviation")
	print(" 7. Full Report")
	print(" 8. Show series")
	print(" 9. Read series from input file")
	print(" 10. Save series to output file")
	print("\n 0. Quit\n")

	option = int(input("Insert option: "))
	return(option);


def dataInput():
	global x
	x = []
	num = int(input("Insert number of elements: "))
	for k in range(num):
		x.append(int(input(f"\nInsert x{k}:")))


def showSeries(x):
	print("\nSeries: ", x, end='')



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

def saveSeries(x):
	outfile = open('input.txt','w')
	for i in x:
		outfile.write(str(i) + '\n')
	outfile.close()
	print('Data written to input.txt')

def readSeries():
	global x
	x = []
	inputFile = open("input.txt",'r')
	for line in inputFile:
		x.append(float(line))
			
def main():
	op = 0
	while (True):
		op = menu()
		os.system("clear")
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
			readSeries()
		elif (op == 10):
			saveSeries(x)
		else:
			break

#Entry point
if __name__ == '__main__':
	main()
		







