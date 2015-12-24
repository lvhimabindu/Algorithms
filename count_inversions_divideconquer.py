import sys

'''

This program implements a divide-and-conquer approach to count the number of inversions in a given array. 

What is an inversion?
- Given an array A, if we have a pair of indices i and j such that i < j and A[i] > A[j], then we refer to such a pair as an inversion. 

Input: An array (or list) of integers or floats or strings.
Output: Number of inversions in the input array (or list). 

Intuition: 
The divide and conquer approach to counting the number of inversions relies heavily on mergesort. The basic idea is to split the computation of total number of inversions
in an array of length n into three parts: number of inversions within the first half + number of inversions within the second half + number of inversions between first and second half. 
This can be achieved by the following steps:
1. Recursively divide the list into two sublists.
2. Repeatedly merge sublists to produce new sorted sublist until there is only one such sublist remaining. This merge routine also computes the number of inversions (alongside sorting the array).   

'''

def count_inv_recursive(arr):
	''' This function implements the merge sort with a twist for counting inversions. 
	It takes an array (possibly unsorted) as input and outputs the number of inversions in the array. '''
	
	n = len(arr)
	
	if n <= 1:				# base condition: if the length of the array is <= 1, then return the array as is.
		return arr, 0

	inv = 0

	sorted_subarray1, temp1 = count_inv_recursive(arr[0:n/2])		# temp1 captures the number of inversions within first half of the array
	sorted_subarray2, temp2 = count_inv_recursive(arr[n/2:n])		# temp2 captures the number of inversions within second half of the array
	
	sorted_array, temp3 = merge(sorted_subarray1,sorted_subarray2)		# temp3 captures the number of inversions between first and second half. 

	return sorted_array, (inv+temp1+temp2+temp3)


def merge(s1,s2):
	''' This function takes as input two sorted lists and merges them into a single sorted list while counting the number of inversions in the complete list '''
	
	n1 = len(s1)
	n2 = len(s2)

	i = 0
	j = 0

	s = []

	num_inv = 0

	while i < n1 and j < n2:		# this means both the pointers i and j are within the respective subarrays
		if s1[i] <= s2[j]:
			s.append(s1[i])
			i += 1
			
		else:
			s.append(s2[j])
			j += 1
			num_inv += (n1-i)


	if i == n1:				# either of i or j (not both) become equal to the respective subarray lengths for the loop to exit. 
		s += s2[j:]
	elif j == n2:
		s += s1[i:]

	return s, num_inv


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

	sarr, inv = count_inv_recursive(arr)
	print "The number of inversions in the array is : %d" % (inv)
