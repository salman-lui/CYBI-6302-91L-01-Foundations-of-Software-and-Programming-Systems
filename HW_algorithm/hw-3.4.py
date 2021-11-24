# Md Salman Rahman
# Machine: 2021 Macbook M1 Pro
#Algorithm 1: O(log n) (logaritgmic time)
import time 
from tabulate import tabulate
import numpy as np
def binarySearch(arr, key, low, high):
   
    while low <= high:
        mid = low + (high - low)//2  #give the index of middle point 
        
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1
    
    
    
#Entry point

arr = [14,46,43,27,57,41,45,21,70]

key = 45

#time 
t0_1 = int(time.time())
for i in range(1000):
	binarySearch(arr, key, 0, len(arr)-1)
t1_1 = int(time.time())
#print("Time interval: ",(t1-t0)*1000/1000," seconds")
time_inter_al_1 = (t1_1-t0_1)*1000/1000


#Algorithm 2: O(n) (linear time)

def LinearSearch(list, k):

    for j in range(0, len(list)):

        if (list[j] == k):

            return j

    return -1

 
#Entry point
 
list = [14,46,43,27,57,41,45,21,70]

k = 45

#time 
t0_2 = int(time.time())
for i in range(1000):
	LinearSearch(list, k)
t1_2 = int(time.time())
#print("Time interval: ",(t1-t0)/1000," seconds")
time_inter_al_2 = (t1_2-t0_2)*1000/1000

# Algorithm 3: O(n log n)(Quasilinear time)

def merge_sort(data):
    if len(data) <= 1:
        return
    
    mid = len(data) // 2
    left_data = data[:mid]
    right_data = data[mid:]
    
    merge_sort(left_data)
    merge_sort(right_data)
    
    left_index = 0
    right_index = 0
    data_index = 0
    
    while left_index < len(left_data) and right_index < len(right_data):
        if left_data[left_index] < right_data[right_index]:
            data[data_index] = left_data[left_index]
            left_index += 1
        else:
            data[data_index] = right_data[right_index]
            right_index += 1
        data_index += 1
    
    if left_index < len(left_data):
        del data[data_index:]
        data += left_data[left_index:]
    elif right_index < len(right_data):
        del data[data_index:]
        data += right_data[right_index:]
    

#Entry point
list = [14,46,43,27,57,41,45,21,70]
#time 
t0_3 = int(time.time())
for i in range(1000):
	merge_sort(list)
t1_3 = int(time.time())
#print("Time interval of Algorithm 3 - O(n log n)",(t1-t0)/1000," seconds")
time_inter_al_3 = (t1_3-t0_3)*1000/1000



# Algorithm 4: O(n^2) (Quadratic time)
def bubbleSort(arr):
    n = len(arr)
 
    # Traverse through all array elements
    for i in range(n-1):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Swap if the element found is greater
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
 
# Driver code to test function bubbleSort
arr = [14,46,43,27,57,41,45,21,70]

t0_4 = int(time.time())
for i in range(1000):
	bubbleSort(arr)
t1_4 = int(time.time())
time_inter_al_4 = (t1_4-t0_4)*1000/1000
#print("Time interval: ",(t1-t0)*1000/1000," seconds")


# Algorithm 5: O(n^3) (Cubic time)

# triple nested loops for finding the solution of multi variable equations
def solution(n):
	answer =[]

# Algorithm 6: O(2^n) (Exponential time)

# fibonacci number finding 
def Fibonacci(n):
    if n < 0:
        print("Input is not correct")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
 
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
 

# Driver code to test function 
#print(Fibonacci(9))
t0_6 = int(time.time())
for i in range(1000):
	Fibonacci(9)
t1_6 = int(time.time())
time_inter_al_6 = (t1_6-t0_6)*1000/1000
#print("Time interval: ",(t1_6-t0_6)*1000/1000," seconds")




# table 

table = [['Algorithm', 'Name', 'Time Interval (seconds)'], [1,"O(log n) (logaritgmic time)",time_inter_al_1], [2,"O(n) (linear time)",time_inter_al_2], [3,"O(n log n)(Quasilinear time)",time_inter_al_3], [4, "O(n^2) (Quadratic time)", time_inter_al_4], [6, "O(2^n) (Exponential time)", time_inter_al_6]]

print(tabulate(table, headers='firstrow', tablefmt='grid'))


# This program displays a simple line graph.
import matplotlib.pyplot as plt
import math
# Plotting Insertion sort T(n) in the interval [1000, 10000]

def main():
	factor = 10000000
	x = []
	y = []
	z = []
	w = []
	for index in range(0, 11,1):
		x.append(index*100000)
		y.append(np.log(x))
		z.append(x)
		w.append(x*np.log(x))
	#print(x)
	#print(y)


'''
	##w[0] = 0    
	#w[1] = 0.08       # Size 1000
	w[2] = 0.2        # Size 2000
	w[3] = 0.7
	w[4] = 1.2
	w[5] = 1.8
	w[6] = 2.6  
	w[7] = 2.7
	w[8] = 3.75
	w[9] = 4.75
	w[10] = 6.5       # Size 100000

'''
# Build the line graph.
	#plt.plot(x, y) and plt.plot(x, z) and plt.plot(x,w)
	#plt.plot(x,w)
	plt.plot(x, y) and plt.plot(x,w)
	#plt.plot(x,w)
    
    
   

	plt.grid(True)

# Display the line graph.
	plt.show()

# Call the main function.
if __name__ == '__main__':
    main()
