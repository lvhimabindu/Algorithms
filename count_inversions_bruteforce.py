import sys

'''

This program implements a naive approach to count the number of inversions in a given array. 

What is an inversion?
- Given an array A, if we have a pair of indices i and j such that i < j and A[i] > A[j], then we refer to such a pair as an inversion. 

Input: An array (or list) of integers or floats or strings.
Output: Number of inversions in the input array (or list). 

Intuition: 
The algorithm implemented here is pretty straightforward. It is akin to selection sort where we compare every pair of elements indexed by some i, j (such that i < j) in the array 
and check if there is an inversion. 

'''

def count_inversions(arr):
	''' This function implements the main functionality to compute the number of inversions in a given array. '''
	
	n = len(arr)
	inv = 0	

	for i in range(n-1):
		for j in range(i+1,n):
			if arr[i] > arr[j]:
				inv += 1

	return inv


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

	print "The number of inversions in the array is : %d" % (count_inversions(arr))
