# hard_savings_account.py
from datetime import datetime

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds."
        elif amount <= 0:
            return "Withdrawal amount must be positive."
        else:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.02):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
        self.transactions = []  # list to store transaction logs

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        self._log_transaction(f"Interest applied: ${interest:.2f}")
        return f"Interest of ${interest:.2f} applied. New balance: ${self.balance:.2f}"

    def deposit(self, amount):
        result = super().deposit(amount)
        self._log_transaction(result)
        return result

    def withdraw(self, amount):
        result = super().withdraw(amount)
        self._log_transaction(result)
        return result

    def _log_transaction(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.transactions.append(f"{timestamp} - {message}")

    def show_transactions(self):
        print("\nTransaction History:")
        for log in self.transactions:
            print(log)


# Example usage
acct = SavingsAccount("Sreeja", 1000, 0.05)
print(acct.deposit(500))
print(acct.withdraw(200))
print(acct.apply_interest())
acct.show_transactions()
