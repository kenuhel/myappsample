
class User:

    pay_raise = 1.05

    def __init__(self, first_name, last_name, pay):
        self.first = first_name
        self.last = last_name
        self.pay = pay

    @property
    def email(self):
        return "{}.{}@gmail.com".format(self.first,self.last)
    
    @property
    def fullname(self):
        return "{} {}".format(self.first,self.last)
    
    def user_pay_raise(self):
        self.pay = int(self.pay * self.pay_raise)
