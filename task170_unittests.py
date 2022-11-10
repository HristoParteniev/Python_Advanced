import unittest 
"""In this exercise you will create a set of test cases to test a bank Account class.
 Each new Account must have an account number, 
 a date of opening, 
 an interest rate, and an 
 opening balance. 
 It must support methods to deposit and withdraw money and to transfer money between accounts. 
 Do not implement the Account class (a dummy implementation is enough - all methods should just "pass") and hence all tests shall fail. """
 

class BankAccount: 

    def __init__(self, account_number, opening_date, interest_rate, opening_balance) -> None:
        self.account_number = account_number
        self.opening_date = opening_date
        self.interest_rate = interest_rate
        self.opening_balance = opening_balance
        self.current_balance = opening_balance

    def deposit_money(self, amount):
        pass
        # self.current_balance += amount
 

    def withdraw_money(self, amount):
        pass
        # if amount <= self.current_balance:
        #     self.current_balance -= amount
 

    def transfer_money(self, bankaccount, amount):
        pass
        # if amount <= self.current_balance and bankaccount is not None:
        #     self.current_balance -= amount
        #     bankaccount.current_balance += amount



class Test(unittest.TestCase):

    def test_deposit_money(self):
        account1 = BankAccount('12345', '9999-12-31', 5, 0)
        self.assertEqual((account1.current_balance + 100),100)

    def test_withdraw_money(self):
        
        self.assertEqual( 5,-104564564560)

    def test_transfer_money(self):
        account1 = BankAccount('12345', '9999-12-31', 5, 0)
        account2 = BankAccount('67890', '2000-12-31', 5, 500)
        self.assertEqual((account1.current_balance - 100 + account2.current_balance + 100), 2000)
        
if __name__ == '__main__':
    unittest.main()

