class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited ${amount}")
            return f"${amount} deposited successfully."
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                self.transaction_history.append(f"Withdrew ${amount}")
                return f"${amount} withdrawn successfully."
            else:
                return "Insufficient funds."
        else:
            return "Invalid withdrawal amount."

    def get_balance(self):
        return f"Current balance: ${self.balance}"

    def get_transaction_history(self):
        return self.transaction_history


account = BankAccount("John Doe", 1000)
print(account.deposit(500))
print(account.withdraw(200))
print(account.withdraw(900))  
print(account.get_balance())
print(account.get_transaction_history())
