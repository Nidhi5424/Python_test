
class InsufficientBalanceError(Exception):
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError("Withdrawal failed: Insufficient balance.")
        else:
            self.balance -= amount
            print("Withdrawal successful! Remaining balance:", self.balance)

account = BankAccount(1000)

print("Your current balance is:", account.balance)

try:
    amt = int(input("Enter amount to withdraw: "))
    account.withdraw(amt)

except InsufficientBalanceError as e:
    print(e)

except ValueError:
    print("Invalid input! Please enter a number.")
