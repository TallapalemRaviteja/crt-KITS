class Bank:
    def interest_rate(self):
        print("Interest Rate: 4%")

class PrivateBank(Bank):
    def interest_rate(self):
        print("Interest Rate: 6%")

obj = PrivateBank()
obj.interest_rate()