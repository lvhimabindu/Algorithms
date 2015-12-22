import unittest
import sys

# Insert the path where the main code file 'karatsuba_recursive_algorithm.py is present 
sys.path.insert(0, '../')

# Import the appropriate function that needs to be called along with the test input. 
from karatsuba_recursive_algorithm import karatsuba_main

class test_karatsuba(unittest.TestCase):
    '''
    Our basic test class
    '''

    def test_zero_mul(self):
        ''' This code tests if multiplying a zero by zero produces the desired result '''
        res = karatsuba_main(0,0)
        self.assertEqual(res, 0)

    def test_zerox_posy(self):
	''' This code tests the scenario when x = 0 and y is a positive integer '''
	res = karatsuba_main(0,1000)
	self.assertEqual(res,0)

    def test_zerox_negy(self):
	''' This code tests the scenario when x = 0 and y is a negative integer '''
	res = karatsuba_main(-500,0)
	self.assertEqual(res,0)

    def test_posx_zeroy(self):
	''' This code tests the scenario when x is a positive integer and y is zero '''
	res = karatsuba_main(250,0)
	self.assertEqual(res,0)

    def test_negx_zeroy(self):
	''' This code tests the scenario when x is a negative integer and y is zero '''
	res = karatsuba_main(-1200,0)
	self.assertEqual(res,0)

    def test_floatx(self):
	''' This code tests the scenario when x is a floating point number '''
	res = karatsuba_main(12.782,13)
	self.assertEqual(res,156)

    def test_floaty(self):
        ''' This code tests the scenario when y is a floating point number '''
        res = karatsuba_main(12,-13.28)
        self.assertEqual(res,-156)	 

    def test_onex_posy(self):
	''' This code tests the scenario when x = 1 and y is a positive integer '''
	res = karatsuba_main(1,10191)
	self.assertEqual(res,10191)

    def test_onex_negy(self):
	''' This code tests the scenario when x = 1 and y is a negative integer '''
	res = karatsuba_main(1,-1098)
	self.assertEqual(res,-1098)

    def test_posx_oney(self):
	''' This code tests the scenario when x is a positive integer and y is 1 '''
	res = karatsuba_main(2089,1)
	self.assertEqual(res,2089)

    def test_negx_oney(self):
	''' This code tests the scenario when x is a negative integer and y is 1 '''
	res = karatsuba_main(-15689,1)
	self.assertEqual(res,-15689)

    def test_strx(self):
	''' This code tests the scenario when x is a string '''
	res = karatsuba_main('abc',128)
	self.assertIsNone(res)

    def test_stry(self):
	''' This code tests the scenario when y is a string '''
	res = karatsuba_main(1089,'d')
	self.assertIsNone(res)

    def test_large(self):
	''' This code tests the multiplication of two large numbers '''
	res = karatsuba_main(1089276,1909831)
	self.assertEqual(res,2080333072356)

    def test_odd_digits(self):
	''' This code tests the multiplication of two numbers which have odd number of digits '''
	res = karatsuba_main(42789,31890)
	self.assertEqual(res,1364541210)

    def test_even_digits(self):
	''' This code tests the multiplication of two even digit numbers '''
	res = karatsuba_main(6789,2391)
	self.assertEqual(res,16232499)

    def test_odd_even(self):
	''' This code tests the multiplication of an even digit number and an odd digit number '''
	res = karatsuba_main(5691,478)
	self.assertEqual(res,2720298)

    def test_single_digit(self):
	''' This code tests the multiplication of a single digit number with other number '''
	res = karatsuba_main(3458,9)
	self.assertEqual(res,31122)

    def test_neg_pos(self):
	''' This code tests the multiplication of a negative number with a positive number '''
	res1 = karatsuba_main(-678,28)
	self.assertEqual(res1,-18984)
	res2 = karatsuba_main(28,-678)
	self.assertEqual(res2,-18984)     

    def test_neg_neg(self):
	''' This code tests the multiplication of two negative numbers '''
	res = karatsuba_main(-281,-9067)
	self.assertEqual(res,2547827)

    def test_square(self):
	''' This code tests the multiplication of the same number twice '''
	res1 = karatsuba_main(13,13)
	self.assertEqual(res1,169)
	res2 = karatsuba_main(6,6)
	self.assertEqual(res2,36)

    def test_primes(self):
	''' This code tests the multiplication of two prime numbers '''
	res = karatsuba_main(31,37)
	self.assertEqual(res,1147)


if __name__ == '__main__':
    unittest.main()
