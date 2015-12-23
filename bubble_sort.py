import sys

''' 

This program implements the bubble sort algorithm. 

Input: A list of integers or floating point numbers or strings.
Output: Sorted list (in ascending order).

Bubble Sort Algorithm: 
Below we discuss the bubble sort technique. 

Intuition:
Bubble sort, sometimes referred to as sinking sort, is a simple sorting algorithm that repeatedly steps through the list to be sorted, 
compares each pair of adjacent items and swaps them if they are in the wrong order. 
The pass through the list is repeated until no swaps are needed, which indicates that the list is sorted. 

Note: This code sorts arrays which comprise of a mix of integer, string and float elements. Ex: If the input array is ['abc',132], then the result is [132,'abc']

Error handling: This code handles scenarios such as empty array input and a single element array. Check the file test_bubble_sort.py for a list of all the test cases. 

'''

def bubble_sort_func(arr):
	''' This function implements the bubble sort. It takes an array (possibly unsorted) as input and outputs a sorted array in ascending order. '''
	
	n = len(arr)
	
	for passes in range(1,n):			# we need n-1 passes, at the end of each pass, the largest element bubbles down to the end of the array
		for i in range(1,n):
			if arr[i-1] > arr[i]:
				# swap arr[i-1] and arr[i]
				temp = arr[i]
				arr[i] = arr[i-1]
				arr[i-1] = temp	

	return arr

if __name__ == '__main__':
	
	try:
		num_elements = input("Enter the number of elements in the array: ")
		num_elements = int(num_elements)
		arr = [0] * num_elements
		for i in range(num_elements):
			arr[i] = input("Enter element no. %d of the array: " % (i+1))
	except Exception:
		print "Please enter valid input!"
		sys.exit(-1)

	

	print "The Sorted Array is: "
	for ele in bubble_sort_func(arr):
		print ele
	
	
