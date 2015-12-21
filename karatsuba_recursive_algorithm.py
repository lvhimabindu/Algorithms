import math

''' 

This file implements the Karatsuba algorithm for multiplying two integers. 

Input: Two integer numbers x and y
Output: The product of x and y computed using Karatsuba method. 

Karatsuba Technique: 
Below we describe the intuition between Karatsuba method and also discuss the details of the algorithm. 

Intuition: Let us assume x and y are n digit numbers. They can be expressed as: 
x = 10^(n/2) * a + b
y = 10^(n/2) * c + d 
The product of x and y can now be written as: 
x * y = 10^n ac + bd + 10^(n/2) [ad + bc] -- (A)

Algorithm: Karatsuba algorithm exploits the fact that x and y can be expressed as shown in Equation (A). Below is the actual algorithm:
1. Recursively compute the product ac
2. Recursively compute the product bd
3. Recursively compute the product (a+b)(c+d)
4. Compute temp = (a+b)(c+d) - ac - bd = (3) - (1) - (2) 
5. Compute the final product as: 10^n * ac + bd + 10^(n/2) * temp

Note: If n is odd then the final product is computed as: 10^(2*floor(n/2)) * ac + bd + 10^(floor(n/2)) * temp

Error Handling: This implementation checks if the input numbers x and y are infact integers and handles the error cases appropriately. 
The code can handle both positive and negative numbers as well as multiplication by zero. 
Floating point numbers are rounded down to the closest integers and then multiplied. 
Check the file test_karatsuba_recursive_algorithm.py for a list of all the test cases. 

'''

def get_digits(num):
	''' This routine counts the number of digits in num and returns the same. '''

	count = 0
	if num == 0:
		return 1
	while num>0:
		count += 1
		num /= 10
	return count

def karatsuba_recursive(x,y):
	''' This is the most important function in this program which implements the karatsuba logic. '''

	# compute the number of digits n
	n = max(get_digits(x),get_digits(y))

	# base condition: if n = 1, then we just return the product of the x and y
	if n == 1:
		return x * y

	tenpowernby2 = int(math.pow(10,n/2))
	tenpowern = int(math.pow(10,2*(n/2)))        # this is not the same as 10^n when n is odd. 

	# compute the values of a, b, c and d
	a = x / tenpowernby2
	b = x % tenpowernby2
	c = y / tenpowernby2
	d = y % tenpowernby2

	# recursively compute the product of a and c
	prod_ac = karatsuba_recursive(a,c)

	# recursively compute the product of b and d
	prod_bd = karatsuba_recursive(b,d)

	# recursively compute the product of (a+b) and (c+d)
	prod_sum = karatsuba_recursive(a+b,c+d)

	temp = prod_sum - prod_ac - prod_bd
        
	return prod_ac*tenpowern + prod_bd + temp*tenpowernby2
		
	
def karatsuba_main(x,y):
	''' This routine checks if x and y are indeed integers and handled the type errors appropriately and then calls the karatsuba_recursive functin.
	It also ensures the sign of the product is returned correctly in the result. '''
	try: 
		x = int(x)
		y = int(y)
	except Exception:
		print "Both x and y should be integers!"
		return -1

	''' If atleast one of the numbers is zero, return 0 ''' 
	if x == 0 or y == 0:
		return 0

	sx = x/abs(x)
	sy = y/abs(y)	

	return sx * sy * karatsuba_recursive(abs(x),abs(y))


if __name__ == '__main__':
	while True:
		try:
			x = input("Enter the value of x: ")
			y = input("Enter the value of y: ")
			break
		except Exception: 
			print "Please enter a valid input (i.e an integer number)!"
			

	prod = karatsuba_main(x,y)
	if prod != -1:
		print "The product of %s and %s is %d" %(x,y,prod)
