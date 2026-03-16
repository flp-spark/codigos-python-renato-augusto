from bank_account import BankAccount
from savings_account import SavingsAccount


bank_account = SavingsAccount()

bank_account.deposit(amount=5)

print(bank_account.get_balance())