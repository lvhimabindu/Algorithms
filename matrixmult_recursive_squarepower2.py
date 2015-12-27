import numpy as np
import sys

'''

This program implements a divide and conquer approach to multiplying two square matrices of size 2^n * 2^n. 

Input: Matrices A and B of dimensions 2^n * 2^n respectively. 
Output: The product matrix A * B of dimensions 2^n * 2^n. 

Approach:
We implement the divide and conquer approach to multiplying square matrices. 
https://en.wikipedia.org/wiki/Matrix_multiplication_algorithm#Divide_and_conquer_algorithm

Note:
This code only handles integer multiplication. 

'''

def fill_up_matrix(orig,mat,rindex,cindex):
	''' This function fills certain elements in matrix orig with those in mat (starting with rindex, cindex) '''

	D = len(mat)
	
	for i in range(D):
		for j in range(D):
			orig[rindex+i,cindex+j] = mat[i,j]		# arrays are passed by references, so just updating here updates the orig matrix in the caller function
			

def matrix_multi_recursive(A,B):
	''' This function computes the product of two square matrices A and B '''
	
	D = len(A)			# D is the dimension of matrices. A and B are of size D * D and D = 2^n for some non-negative integer n

	if D == 1:
                return np.array([[A[0,0] * B[0,0]]])

	# Note that A and B are square matrices and are of dimensions 2^n * 2^n
	# Below are the 8 products that need to be computed 

	A11B11 = matrix_multi_recursive(A[:D/2,:D/2], B[:D/2,:D/2])
	A12B21 = matrix_multi_recursive(A[:D/2,D/2:D], B[D/2:D,:D/2])
	A11B12 = matrix_multi_recursive(A[:D/2,:D/2], B[:D/2,D/2:D])
	A12B22 = matrix_multi_recursive(A[:D/2,D/2:D], B[D/2:D,D/2:D])
	A21B11 = matrix_multi_recursive(A[D/2:D,:D/2], B[:D/2,:D/2])
	A22B21 = matrix_multi_recursive(A[D/2:D,D/2:D], B[D/2:D,:D/2])
	A21B12 = matrix_multi_recursive(A[D/2:D,:D/2], B[:D/2,D/2:D])
	A22B22 = matrix_multi_recursive(A[D/2:D,D/2:D], B[D/2:D,D/2:D])
	
	# Summing products above to get D/2 * D/2 matrices
		
   	LT = A11B11 + A12B21			# left top
	RT = A11B12 + A12B22			# right top
	LB = A21B11 + A22B21			# left bottom
	RB = A21B12 + A22B22			# right bottom

	res = np.zeros(shape=(D,D),dtype=int)

	fill_up_matrix(res,LT,0,0)
	fill_up_matrix(res,RT,0,D/2)
	fill_up_matrix(res,LB,D/2,0)
	fill_up_matrix(res,RB,D/2,D/2)
	
	return res
		
def print_matrix(mat):
	''' This function prints a matrix in the readable format '''
	''' Input: a matrix in the form of a 2-d numpy array '''

	mat = mat.tolist()	
	M = len(mat)
	N = len(mat[0])

	for i in range(M):
                s  = ""
                for j in range(N):
                        s += str(mat[i][j]) + " "
                print s

def is_power_of_2(num):
	''' This function checks if a given num is a power of 2 '''

	return (num != 0) and ((num & (num-1)) == 0)

if __name__ == '__main__':
	
	try:
		m1 = int(input("Enter the number of rows in matrix 1: "))
		n1 = int(input("Enter the number of columns in matrix 1: "))
		m2 = int(input("Enter the number of rows in matrix 2: "))
		n2 = int(input("Enter the number of columns in matrix 2: "))
	
		if m1 == 0 or n1 == 0 or m2 == 0 or n2 == 0:
			print "The number of elements cannot be zero!"
			raise Exception

		if m1 != n1 or m1 != m2 or m1 != n2 or (not is_power_of_2(m1)):
			print "Please input a square matrix of dimensions 2^n * 2^n!"
			raise Exception
		
		A = np.zeros(shape=(m1,n1),dtype=int)
		B = np.zeros(shape=(m2,n2),dtype=int)
		
		for i in range(m1):
			for j in range(n1):
				A[i,j] = input("Enter element (%d,%d) of the matrix 1: " % (i+1,j+1))
				if isinstance(A[i,j],int):
					continue
				else:
					print "Elements of the matrices can only be integers!"
					raise Exception

		for i in range(m2):
                        for j in range(n2):
                                B[i,j] = input("Enter element (%d,%d) of the matrix 2: " % (i+1,j+1))
                                if isinstance(B[i,j],int):
                                        continue
                                else:
					print "Elements of the matrices can only be integers!"
                                        raise Exception	


	except Exception:
                print "Input entered is not valid!"
                sys.exit(-1)

	print "Matrix 1: "
	print_matrix(np.array(A))
	print "Matrix 2: "
	print_matrix(np.array(B))

	result = matrix_multi_recursive(np.array(A),np.array(B))
	print "The result of the multiplication is: "
	print_matrix(result)
