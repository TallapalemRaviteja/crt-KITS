class Ticket:
    def price(self):
        print("Ticket Price: ₹150")

class VIPTicket(Ticket):
    def price(self):
        print("Ticket Price: ₹500")

vip = VIPTicket()
vip.price()