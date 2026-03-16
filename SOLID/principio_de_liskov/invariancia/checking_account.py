from bank_account import BanckAccount

class CheckingAccount(BanckAccount):

    def __init__(self, over_draft_limit:float):
        self.over_draft_limit = over_draft_limit
        

    def withdraw(self, amount):

        if amount <= 0:
            print('O valor do saque deve ser positivo')

        available_balance = self.balance + self.over_draft_limit

        if amount > available_balance:
            print('Saldo insuficiente e limite do cheque especial exedido')

        self.balance = self.balance - amount


        return super().withdraw(amount)
        