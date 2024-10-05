class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = account_balance = 0

    def deposit(self, amount):
        self.account_balance += amount
        return self.account_balance

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if self.account_balance > amount:
            self.account_balance -= amount
            return True
        else:
            print("Insufficient funds.")
            return False

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")