import sys

''' 

This program implements the selection sort algorithm. 

Input: A list of integers or floating point numbers or strings.
Output: Sorted list (in ascending order).

Selection Sort Algorithm: 
Below we discuss the selection sort technique. 

Intuition:
Selection sort is one of the most intuitive sorting techniques. 
The algorithm divides the input list into two parts: the sublist of items already sorted, which is built up from left to right at the front (left) of the list, 
and the sublist of items remaining to be sorted that occupy the rest of the list. 
Initially, the sorted sublist is empty and the unsorted sublist is the entire input list. 
The algorithm proceeds by finding the smallest (or largest, depending on sorting order) element in the unsorted sublist, exchanging (swapping) it with the leftmost 
unsorted element (putting it in sorted order), and moving the sublist boundaries one element to the right.

Note: This code sorts arrays which comprise of a mix of integer, string and float elements. Ex: If the input array is ['abc',132], then the result is [132,'abc']

Error handling: This code handles scenarios such as empty array input and a single element array. Check the file test_sorting_algorithms.py for a list of all the test cases. 

'''

def selection_sort_func(arr):
	''' This function implements the selection sort. It takes an array (possibly unsorted) as input and outputs a sorted array in ascending order. '''
	
	n = len(arr)
	for i in range(0,n-1):

		min_index = i				        # iteration to find the least element suitable for position i
		for j in range(i+1,n):
			if arr[j] < arr[min_index]: 
				min_index = j
		
		if min_index != i:				# if the minimum element is not the current element
			temp = arr[i]
			arr[i] = arr[min_index]
			arr[min_index] = temp

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
	for ele in selection_sort_func(arr):
		print ele
	
	
