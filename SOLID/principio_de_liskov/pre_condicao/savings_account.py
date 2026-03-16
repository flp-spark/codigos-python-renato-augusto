from bank_account import BankAccount


class SavingsAccount(BankAccount):

    def deposit(self, amount):
        if amount < 10:
            print('O deoposito minimo é de 10 para conta poupança')

        return super().deposit(amount)

