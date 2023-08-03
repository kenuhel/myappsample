import unittest

from my_sum import sum
from fractions import Fraction
from my_sum import blanckSpaces

class TestSum(unittest.TestCase):

    def test_list_Sum(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result,6)

    def test_list_NegativeSum(self):
        """
        Test that it can sum negative numbers
        """
        data2 = [1,3,-1]
        result2 = sum(data2)
        self.assertEqual(result2, 3)

    def test_list_fraction(self):
        """
        Test that it can sum list of fractions
        """
        data3 = [Fraction(1,4), Fraction(1,4), Fraction(2,5)]
        result3 = sum(data3)
        self.assertEqual(result3, Fraction(9,10))

    def test_bad_type(self): 
        data = "banana"
        with self.assertRaises(TypeError): # estos es como un try catch
            result = sum(data)

    def test_count_blanks(self):
        data = "Today is Monday"
        result4 = blanckSpaces(data)
        self.assertLess(result4, 10)

if __name__ == "__main__":
    unittest.main()

