#
# Test 2
#

import unittest

from employee import Employee
from fractions import Fraction

class TesEmployee(unittest.TestCase):

    def setUp (self):
        print("setUp")
        self.emp1 = Employee("john","rojas",600000)
        self.emp2 = Employee("ane","ramirez",700000)

    def tearDown(self) :
        print("tearDown \n")


    def test_email(self):
        print("test_email")
        self.assertEqual(self.emp1.email, "john.rojas@gmail.com")
        self.assertEqual(self.emp2.email, "ane.ramirez@gmail.com")

        self.emp1.first = "Ken"
        self.emp2.first = "Gyuon"

        self.assertEqual(self.emp1.email, "Ken.rojas@gmail.com")
        self.assertEqual(self.emp2.email, "Gyuon.ramirez@gmail.com")
    

    def test_fullName(self):
        print("test_fullName")
        self.assertEqual(self.emp1.fullName, "john rojas")
        self.assertEqual(self.emp2.fullName, "ane ramirez")

        self.emp1.first = "Ken"
        self.emp2.first = "Gyuon"

        self.assertEqual(self.emp1.fullName, "Ken rojas")
        self.assertEqual(self.emp2.fullName, "Gyuon ramirez")

    def test_pay(self):
        print("test_pay")
        self.emp1.apply_raise()
        self.emp2.apply_raise()

        self.assertEqual(self.emp1.pay, 630000)
        self.assertEqual(self.emp2.pay, 735000)


if __name__ == "__main__":
    unittest.main()