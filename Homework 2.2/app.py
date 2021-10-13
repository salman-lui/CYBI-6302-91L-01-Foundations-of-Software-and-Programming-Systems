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
import array as arr
import math


x = arr.array('i')

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
	global x
	num = int(input("Insert number of elements: "))
	for k in range(num):
		x.append(int(input(f"\nInsert x{k}:")))







def showMinimum(x):
	min=x[0]
	for i in range(len(x)):
		if x[i]<min:
			min=x[i]

	print("\nMinimum: ", min)






def showMaximum(x):
	max=x[0]
	for i in range(len(x)):
		if x[i]>max:
			max=x[i]

	print("\nMaximum: ", max)

def showSum(x):
	sum=0
	for i in range(len(x)):
		sum+=x[i]
	print("\nShow sum: ", sum)


def showMean(x):
	sum=0
	for i in range(len(x)):
		sum+=x[i]
	mean=sum/len(x)
	return mean   # we use this mean in standard deviation thats why I return this and print it separately 
	


def showStandard_Deviation(x):
	mean=showMean(x)
	var=0
	for i in range(len(x)):
		var += (((mean-x[i])**2)/len(x))

	sd=math.sqrt(var)
	print(f'\nVariance = {var} & Standard Deviation = {sd}')  # here the variance and standard deviation is population variance and standard deviation not for sample


def showFull_Report(x):
	showMinimum(x)
	showMaximum(x)
	showSum(x)
	print("\nShow mean: ", showMean(x))
	showStandard_Deviation(x)
	showSeries(x)

def showSeries(x):
	q=[]    # define a list so that we can store the series in this list
	for i in range(len(x)):
		#q+=str(x[i])
		q.append(str(x[i]))
	print("\nSeries: ", q)
	


def main():
	op = 0
	while (True):
		op = menu()
		os.system("cls")
		if (op == 1):
			dataInput()
		elif (op == 2):
			showMinimum(x)
		elif (op == 3):
			showMaximum(x)
		elif (op==4):
			showSum(x)
		elif (op == 5):
			print("\nShow mean: ", showMean(x))
		elif (op == 6):
			showStandard_Deviation(x)
		elif (op==7):
			showFull_Report(x)
		elif (op==8):
			showSeries(x)
		else:
			break


main()