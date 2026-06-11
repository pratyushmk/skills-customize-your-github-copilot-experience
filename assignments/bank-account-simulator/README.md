# 📘 Assignment: Bank Account Simulator

## 🎯 Objective

Use Python classes to model a bank account and implement methods for deposits, withdrawals, and balance checks.

## 📝 Tasks

### 🛠️ Define the `BankAccount` class

#### Description
Create a `BankAccount` class with attributes and methods to manage account operations.

#### Requirements
Completed program should:

- Define a `BankAccount` class with `account_holder` and `balance` attributes.
- Initialize `balance` to `0` by default.
- Include a `deposit(amount)` method that adds money and verifies the amount is positive.
- Include a `withdraw(amount)` method that subtracts money only when the account has sufficient funds.
- Include a `get_balance()` method that returns the current balance.

### 🛠️ Add transaction validation

#### Description
Ensure deposits and withdrawals are validated before updating the balance.

#### Requirements
Completed program should:

- Prevent depositing zero or negative amounts.
- Prevent withdrawing more than the available balance.
- Return or raise clear error messages for invalid operations.
- Keep valid transactions applied correctly to the account balance.

### 🛠️ Create a simple user flow

#### Description
Build a small command-line flow that creates a bank account and performs sample operations.

#### Requirements
Completed program should:

- Create a `BankAccount` instance for a sample account holder.
- Deposit money, withdraw money, and print the resulting balance.
- Show messages like `Deposit successful`, `Withdrawal successful`, or `Insufficient funds`.
- Example usage should demonstrate at least one successful deposit and one failed withdrawal.
