class BankAccount:
    def __init__(self, account_holder: str, balance: float = 0.0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        return f"Deposit successful: ${amount:.2f}"

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return f"Withdrawal successful: ${amount:.2f}"

    def get_balance(self):
        return self.balance


if __name__ == "__main__":
    account = BankAccount("Alex")
    print(account.deposit(100))
    try:
        print(account.withdraw(30))
    except ValueError as error:
        print(error)
    try:
        print(account.withdraw(100))
    except ValueError as error:
        print(error)
    print(f"Final balance: ${account.get_balance():.2f}")
