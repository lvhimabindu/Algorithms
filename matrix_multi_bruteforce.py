import sys

'''

This program implements the most straight forward approach to multiplying two matrices. 

Input: Matrices A and B of dimensions m * k and k * n respectively. 
Output: The product matrix A * B of dimensions m * n. 

Approach:
Each element of the product matrix P_{i,j} can be computed as: P_{i,j} = \sum_{k} A_{i,k} * B_{k,j}.
In order to compute the product matrix, we iterate over all possible values of i and j and compute P_{i,j} as mentionend above. 

'''

def matrix_multiplication(A,B):
	''' This function computes the product of two matrices A and B '''
	
	M = len(A)
	N = len(B[0])
	K = len(B)
	
	res = [[0] * N for i in range(M)]

	for i in range(M):
		for j in range(N):
			for p in range(K):
				res[i][j] += A[i][p] * B[p][j]

	return res
		
def print_matrix(mat):
	''' This function prints a matrix in the readable format '''
	
	M = len(mat)
	N = len(mat[0])

	for i in range(M):
                s  = ""
                for j in range(N):
                        s += str(mat[i][j]) + " "
                print s

if __name__ == '__main__':
	
	try:
		m1 = int(input("Enter the number of rows in matrix 1: "))
		n1 = int(input("Enter the number of columns in matrix 1: "))
		m2 = int(input("Enter the number of rows in matrix 2: "))
		n2 = int(input("Enter the number of rows in matrix 2: "))
		
		if m1 == 0 or n1 == 0 or m2 == 0 or n2 == 0:
			print "The number of elements cannot be zero!"
			sys.exit(-1)

		if n1 != m2:
			print "The number of columns of matrix 1 should be the same as the number of rows of matrix 2"
			sys.exit(-1)
		
		A = [[0] * n1 for i in range(m1)]
		B = [[0] * n2 for i in range(m2)]
		
		for i in range(m1):
			for j in range(n1):
				A[i][j] = input("Enter element (%d,%d) of the matrix 1: " % (i+1,j+1))
				if isinstance(A[i][j],int) or isinstance(A[i][j],float):
					continue
				else:
					raise Exception
		
		for i in range(m2):
                        for j in range(n2):
                                B[i][j] = input("Enter element (%d,%d) of the matrix 2: " % (i+1,j+1))
                                if isinstance(B[i][j],int) or isinstance(B[i][j],float):
                                        continue
                                else:
                                        raise Exception	

	except Exception:
                print "Please enter valid input!"
                sys.exit(-1)

	print "Matrix 1: "
	print_matrix(A)
	print "Matrix 2: "
	print_matrix(B)

	result = matrix_multiplication(A,B)
	print "The result of the multiplication is: "
	print_matrix(result)
