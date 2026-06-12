class Customer:
    def delivery_charge(self):
        print("Delivery Charge: ₹50")

class PrimeCustomer(Customer):
    def delivery_charge(self):
        print("Delivery Charge: ₹20")

prime = PrimeCustomer()
prime.delivery_charge()