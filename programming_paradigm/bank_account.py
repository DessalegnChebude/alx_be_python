class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = account_balance = 0

    def deposit(amount):
        self.account_balance += amount
        return self.account_balance

    def withdraw(amount):
        if self.account_balance > amount:
            return True
        else:
            return False

    def display_balance():
        print(f"The current balance is: ${self.account_balance}")