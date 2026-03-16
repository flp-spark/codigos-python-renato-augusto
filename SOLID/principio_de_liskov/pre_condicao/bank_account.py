

class BankAccount:

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount:float):

        if amount <= 0:
            print('Deposito invalido, o valor deve ser positivo')

        self.balance = self.balance + amount

    def get_balance(self):

        return self.balance
        