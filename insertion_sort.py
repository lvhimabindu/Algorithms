import sys

''' 

This program implements the insertion sort algorithm. 

Input: A list of integers or floating point numbers or strings.
Output: Sorted list (in ascending order).

Insertion Sort Algorithm: 
Below we discuss the insertion sort technique. 

Intuition:
Insertion sort works the same way as one would sort a bridge or gin rummy hand, i.e. starting with an empty left hand and the cards face down on the table. 
One card at a time is then removed from the table and inserted into the correct position in the left hand. 
To find the correct position for a card, it is compared with each of the cards already in the hand, from right to left. 

Note: This code sorts arrays which comprise of a mix of integer, string and float elements. Ex: If the input array is ['abc',132], then the result is [132,'abc']

Error handling: This code handles scenarios such as empty array input and a single element array. Check the file test_insertion_sort.py for a list of all the test cases. 

'''

def insertion_sort_func(arr):
	''' This function implements the insertion sort. It takes an array (possibly unsorted) as input and outputs a sorted array in ascending order. '''
	
	n = len(arr)
	
	for i in range(1,n):
		
		key = arr[i]			# assign to key the value of the current element
		
		j = i - 1
		
		while j >= 0 and arr[j] > key:
			# copy the jth element to j+1th element, shifting the position by one to the right. 
			arr[j+1] = arr[j]	
			j -= 1

		arr[j+1] = key			# copy key in the j+1th position

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
	for ele in insertion_sort_func(arr):
		print ele
	
	
