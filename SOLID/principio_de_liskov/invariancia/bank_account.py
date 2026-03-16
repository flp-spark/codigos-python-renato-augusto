class BanckAccount:

    def __init__(self, balance:float=0):
        self.balance = balance

    def withdraw(self, amount:float):

        if amount <= 0 :
            print('O valor do saque deve ser positivo')
        
        if amount > self.balance:
            print('Saldo insuficiente. Saldop não pode ficar negativo')

        self.balance = self.balance - amount

    def get_balance(self):

        return self.balance
        