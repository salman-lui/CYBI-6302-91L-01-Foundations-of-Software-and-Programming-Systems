#Author: Md Salman Rahman
'''
Complete the implementation in Python of the pending functionality 6 and 7 in the menu-driven procedural program that 
shows on the console statistic values from a series of n integers numbers inserted by the user. 
Use as reference the C++ prototype developed in Lab 2.2.
BASIC STATISTIC CALCULATOR:
1.- Insert Series
2.- Minimum
3.- Maximum
4.- Sum
5.- Arithmetic Mean
6.- Standard Deviation
7.- Full Report
8.- Show Series
0.- Quit
'''

import os

import math


x1, x2, x3 = 0, 0, 0

def menu():
	option = 0
	print("\n\nBasic Calculator\n")
	print(" 1. Insert series")
	print(" 2. Minimum")
	print(" 3. Maximum")
	print(" 4. Sum")
	print(" 5. Arithmetic Mean")
	print(" 6. Standard Deviation")
	print(" 7. Full Report")
	print(" 8. Show Series")
	print("\n 0. Quit\n")

	option = int(input("Insert option: "))
	return(option)


def dataInput():
	global x1, x2, x3
	x1 = int(input("\nInsert x1: "))
	x2 = int(input("\nInsert x2: "))
	x3 = int(input("\nInsert x3: "))




def showMinimum(x1, x2, x3):
	min = x1
	if (x2<min):
		min = x2
	if (x3<min):
		min = x3
	print("\nMinimum: ", min)



def showMaximum(x1, x2, x3):
	max = x1
	if (x2>max):
		max = x2
	if (x3>max):
		max = x3
	print("\nMaximum: ", max)



def showSum(x1,x2,x3):
	print("\nShow sum: ",(x1+x2+x3))



def showMean(x1, x2, x3):
	print("\nShow mean: ", (x1+x2+x3)/3)


def showStandard_Deviation(x1,x2,x3):
	mean =(x1+x2+x3)/3
	variance = ((mean-x1)**2+(mean-x2)**2+(mean-x3)**2)/3
	sd=math.sqrt(variance)

	print(f'\nVariance = {variance} & Standard Deviation = {sd}')


def showFull_Report(x1,x2,x3):
	showSeries(x1,x2,x3)
	showMinimum(x1,x2,x3)
	showMaximum(x1,x2,x3)
	showSum(x1,x2,x3)
	showMean(x1,x2,x3)
	showStandard_Deviation(x1,x2,x3)
	showSeries(x1,x2,x3)


def showSeries(x1, x2, x3):
	print("\nSeries: ", x1, x2, x3)
	


def main():
	op = 0
	while (True):
		op = menu()
		os.system("clear")
		if (op == 1):
			dataInput()
		elif (op == 2):
			showMinimum(x1,x2,x3)
		elif (op == 3):
			showMaximum(x1,x2,x3)
		elif (op==4):
			showSum(x1,x2,x3)
		elif (op == 5):
			showMean(x1,x2,x3)
		elif (op == 6):
			showStandard_Deviation(x1,x2,x3)
		elif (op==7):
			showFull_Report(x1,x2,x3)
		elif (op==8):
			showSeries(x1,x2,x3)
		else:
			break


main()