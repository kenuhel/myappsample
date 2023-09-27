import unittest
from dir1 import User

class test_user(unittest.TestCase):

   
    def setUp(self):
        print("setUp")
        self.emp1 = User("John","Looman",80000)
        self.emp2 = User("Ane","Hoot",90000)
    
    def tearDown(self):
        print("tearDown \n")

    def test_email(self):
        print("Testing email")
        self.assertEqual(self.emp1.email, "John.Looman@gmail.com")
        self.assertEqual(self.emp2.email, "Ane.Hoot@gmail.com")

        self.emp1.first = "Ken"
        self.emp2.first = "Fer"

        self.assertEqual(self.emp1.email, "Ken.Looman@gmail.com")
        self.assertEqual(self.emp2.email, "Fer.Hoot@gmail.com")

    def test_fullname(self):
        print("Testing fullname")
        self.assertEqual(self.emp1.fullname, "John Looman")
        self.assertEqual(self.emp2.fullname, "Ane Hoot")

        self.emp1.last = "Rojas"
        self.emp2.last = "Campos"

        self.assertEqual(self.emp1.fullname, "John Rojas")
        self.assertEqual(self.emp2.fullname, "Ane Campos")

    def test_payment_raise(self):
        print("Testing User_pay_raise")
        self.emp1.user_pay_raise()
        self.emp2.user_pay_raise()

        self.assertEqual(self.emp1.pay, 84000)
        self.assertEqual(self.emp2.pay, 94500)

        



if __name__ == "__main__":
    unittest.main()