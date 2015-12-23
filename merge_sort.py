import sys

''' 

This program implements the merge sort algorithm. 

Input: A list of integers or floating point numbers or strings.
Output: Sorted list (in ascending order).

Merge Sort Algorithm: 
Below we discuss the merge sort technique. 

Intuition:
Conceptually, a merge sort works as follows:
1. Recursively divide the list into two sublists.
2. Repeatedly merge sublists to produce new sorted sublist until there is only one such sublist remaining.  

Note: This code sorts arrays which comprise of a mix of integer, string and float elements. Ex: If the input array is ['abc',132], then the result is [132,'abc']

Error handling: This code handles scenarios such as empty array input and a single element array. Check the file test_bubble_sort.py for a list of all the test cases. 

'''

def merge_sort_func(arr):
	''' This function implements the merge sort. It takes an array (possibly unsorted) as input and outputs a sorted array in ascending order. '''
	
	n = len(arr)
	
	if n <= 1:				# base condition: if the length of the array is <= 1, then return the array as is.
		return arr

	sorted_subarray1 = merge_sort_func(arr[0:n/2])
	sorted_subarray2 = merge_sort_func(arr[n/2:n])
	
	sorted_array = merge(sorted_subarray1,sorted_subarray2)	

	return sorted_array


def merge(s1,s2):
	''' This function takes as input two sorted lists and merges them into a single sorted list '''
	
	n1 = len(s1)
	n2 = len(s2)

	i = 0
	j = 0

	s = []

	while i < n1 and j < n2:		# this means both the pointers i and j are within the respective subarrays
		if s1[i] <= s2[j]:
			s.append(s1[i])
			i += 1
			
		else:
			s.append(s2[j])
			j += 1

	if i == n1:				# either of i or j (not both) become equal to the respective subarray lengths for the loop to exit. 
		s += s2[j:]
	elif j == n2:
		s += s1[i:]

	return s


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
	for ele in merge_sort_func(arr):
		print ele
	
	
