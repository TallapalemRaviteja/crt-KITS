class User:
    def __init__(self, name):
        self.name = name


class Wallet:
    def __init__(self, balance):
        self.balance = balance
        self.transactions = []

    def add_money(self, amount):
        self.balance += amount
        self.transactions.append(f"Added ₹{amount}")

    def transfer_money(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Transferred ₹{amount}")
            return True
        return False

    def show_balance(self):
        return self.balance


class Transaction:
    def __init__(self, user, wallet):
        self.user = user
        self.wallet = wallet

    def generate_receipt(self, opening_balance, transfer_amount):
        print("=" * 50)
        print("          TRANSACTION RECEIPT")
        print("=" * 50)
        print(f"\nUser Name       : {self.user.name}")
        print(f"\nOpening Balance : ₹{opening_balance}")
        print(f"\nTransfer Amount : ₹{transfer_amount}")
        print(f"\nCurrent Balance : ₹{self.wallet.show_balance()}")
        print("\nStatus          : SUCCESSFUL")
        print("\n" + "=" * 50)


user_name = input("User Name: ")
balance = int(input("Wallet Balance: "))
transfer = int(input("Transfer Amount: "))

user = User(user_name)
wallet = Wallet(balance)

opening_balance = wallet.show_balance()

if wallet.transfer_money(transfer):
    transaction = Transaction(user, wallet)
    transaction.generate_receipt(opening_balance, transfer)
else:
    print("Insufficient Balance!")