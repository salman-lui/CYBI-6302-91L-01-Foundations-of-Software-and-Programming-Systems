# Question 2
# Write the python code for reading a real number from the keyboard and 
# for writing that number on the console with two digits of precision in the decinal part. 
# If the conversion from the input to a real number is not possible, the output will be the warning  "The input is not a real number".

#real_number = float(input("Please Enter a real number: \n"))

def main():
	real_number= input("Please enter a number:")
	try:
		conversion=float(real_number)
		print("The number with two digit of precision is: ", f'{conversion:.2f}')
	except:
		print("The input is not a real number")

# Call the main function.
if __name__ == '__main__':
    main()