import numpy as np
import sys

'''

This program implements a divide and conquer approach to multiplying two generic matrices. 

Input: Matrices A and B of dimensions m * k and k * n respectively. 
Output: The product matrix A * B of dimensions m * n. 

Approach:
We implement the divide and conquer approach to multiplying matrices [both square and non-square]. 
https://en.wikipedia.org/wiki/Matrix_multiplication_algorithm#Divide_and_conquer_algorithm

Note:
This code only handles integer multiplication. 

'''

def fill_up_matrix(orig,mat,rindex,cindex):
	''' This function fills certain elements in matrix orig with those in mat (starting with rindex, cindex) '''

	D1 = mat.shape[0]
	D2 = mat.shape[1]

	for i in range(D1):
		for j in range(D2):
			orig[rindex+i,cindex+j] = mat[i,j]		# arrays are passed by references, so just updating here updates the orig matrix in the caller function
			

def squarepower2_recursive(A,B,D):
	''' This function computes the product of two square matrices A and B of size 2^n * 2^n'''
	
	if D == 1:
                return np.array([[A[0,0] * B[0,0]]])

	# Note that A and B are square matrices and are of dimensions 2^n * 2^n
	# Below are the 8 products that need to be computed 

	A11B11 = squarepower2_recursive(A[:D/2,:D/2], B[:D/2,:D/2], D/2)
	A12B21 = squarepower2_recursive(A[:D/2,D/2:D], B[D/2:D,:D/2], D/2)
	A11B12 = squarepower2_recursive(A[:D/2,:D/2], B[:D/2,D/2:D], D/2)
	A12B22 = squarepower2_recursive(A[:D/2,D/2:D], B[D/2:D,D/2:D], D/2)
	A21B11 = squarepower2_recursive(A[D/2:D,:D/2], B[:D/2,:D/2], D/2)
	A22B21 = squarepower2_recursive(A[D/2:D,D/2:D], B[D/2:D,:D/2], D/2)
	A21B12 = squarepower2_recursive(A[D/2:D,:D/2], B[:D/2,D/2:D], D/2)
	A22B22 = squarepower2_recursive(A[D/2:D,D/2:D], B[D/2:D,D/2:D], D/2)
	
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

def squarenotpower2_recursive(A,B,D):
	''' This function multiples two square matrices whose dimensions are not powers of 2 '''
	''' We split first matrix horizontally and second matrix vertically '''
	''' Note that this function will exit only from matrix_multi_recursive '''

	A1B1 = matrix_multi_recursive(A[:D/2,:], B[:,:D/2])
	A1B2 = matrix_multi_recursive(A[:D/2,:], B[:,D/2:])
	A2B1 = matrix_multi_recursive(A[D/2:,:], B[:,:D/2])
	A2B2 = matrix_multi_recursive(A[D/2:,:], B[:,D/2:])

	res = np.zeros(shape=(D,D),dtype=int)
	
	fill_up_matrix(res,A1B1,0,0)
	fill_up_matrix(res,A1B2,0,D/2)
	fill_up_matrix(res,A2B1,D/2,0)
	fill_up_matrix(res,A2B2,D/2,D/2)

	return res
	
def longerm1_recursive(A,B,M,N,K):
	''' This function multiples two non-square matrices such that the number of rows in A is much larger than the rest of dimensions '''
	''' We split first matrix horizontally '''

	A1B = matrix_multi_recursive(A[:M/2,:], B)
	A2B = matrix_multi_recursive(A[M/2:,:], B)

	res = np.zeros(shape=(M,K),dtype=int)

	fill_up_matrix(res,A1B,0,0)
	fill_up_matrix(res,A2B,M/2,0)

	return res
	

def longern1_recursive(A,B,M,N,K):
	''' This function multiples two non-square matrices such that the number of columns in A (number of rows in B) is much larger than the rest of dimensions '''
	''' We split first matrix vertically and second matrix horizontally '''

	A1B1 = matrix_multi_recursive(A[:,:N/2], B[:N/2,:])
	A2B2 = matrix_multi_recursive(A[:,N/2:], B[N/2:,:])

	# summing products above to get the final result

	res = A1B1 + A2B2

	return res

def longern2_recursive(A,B,M,N,K):
	''' This function multiples two non-square matrices such that the number of columns in B is much larger than the rest of dimensions '''
	''' We split second matrix horizontally '''

	AB1 = matrix_multi_recursive(A,B[:,:K/2])
	AB2 = matrix_multi_recursive(A,B[:,K/2:])

	res = np.zeros(shape=(M,K),dtype=int)
	
	fill_up_matrix(res,AB1,0,0)
	fill_up_matrix(res,AB2,0,K/2)

	return res
	

def matrix_multi_recursive(A,B):
	''' This function checks the dimensions of the matrices and call the appropriate function to multiply the matrices '''

	m = A.shape[0]
	k = A.shape[1]
	n = B.shape[1]

	if m == k and k == n and is_power_of_2(m):			#square matrix with dimensions which are powers of 2
		return squarepower2_recursive(A,B,m)

	elif m == k and k == n:						#square matrix (where dimensions are not powers of 2)
		return squarenotpower2_recursive(A,B,m)

	elif max(m,k,n) == m:						# if number of rows of first matrix are much larger than other dimensions
		return longerm1_recursive(A,B,m,k,n)

	elif max(m,k,n) == k:
		return longern1_recursive(A,B,m,k,n)				# if number of columns of first matrix (or rows of second matrix) are larger than other dimensions

	
	return longern2_recursive(A,B,m,k,n)					# the only scenario left is where the number of columns of second matrix are larger than other dimensions

 	
		
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

		if n1 != m2:									# not suitable for multiplication 
			print "Please input matrices of dimensions m x k and k x n!"
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
