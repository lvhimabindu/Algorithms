import unittest
import sys

# Insert the path where the main code file is present 
sys.path.insert(0, '../')
print sys.path

# Import the appropriate function that needs to be called along with the test input. 
from selection_sort import selection_sort_func

class test_sort(unittest.TestCase):
    '''
    Our basic test class
    '''

    def test_emptylist(self):
        ''' check for empty list input '''
        res = selection_sort_func([])
        self.assertListEqual(res, [])

    def test_singleelement(self):
	''' check for a list with a single element '''
	res = selection_sort_func([5])
	self.assertListEqual(res, [5])

    def test_positiveint(self):
	''' check for a list of positive integers '''
	res = selection_sort_func([970,10001,567789,23,1092,2435,58])
	self.assertListEqual(res,[23,58,970,1092,2435,10001,567789])

    def test_negativeint(self):
	''' check for a list of negative integers '''
	res = selection_sort_func([-28,-42,-12,-11,-31,-5,-58])
	self.assertListEqual(res,[-58,-42,-31,-28,-12,-11,-5])

    def test_string(self):
	''' check for a list of strings '''
	res = selection_sort_func(['zyx','rst','aaa','abe','aef','aab'])
	self.assertListEqual(res,['aaa','aab','abe','aef','rst','zyx'])

    def test_mix(self):
	''' check for a list which is a mixture of integers, strings, floats '''
	res = selection_sort_func([23.27,23,13,10,'abc','zyx','rst',13.23])
	self.assertListEqual(res,[10,13,13.23,23,23.27,'abc','rst','zyx'])

if __name__ == '__main__':
    unittest.main()
