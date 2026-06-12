class Customer:
    def __init__(self, customer_name):
        self.customer_name = customer_name


class Movie:
    def __init__(self, movie_name, ticket_price):
        self.movie_name = movie_name
        self.ticket_price = ticket_price


class Booking:
    def __init__(self, customer, movie, number_of_tickets):
        self.customer = customer
        self.movie = movie
        self.number_of_tickets = number_of_tickets

    def calculate_amount(self):
        return self.movie.ticket_price * self.number_of_tickets

    def book_ticket(self):
        print("Ticket booked successfully!")

    def generate_receipt(self):
        total_amount = self.calculate_amount()
        print("=" * 50)
        print("            MOVIE BOOKING RECEIPT")
        print("=" * 50)
        print()
        print(f"Customer Name   : {self.customer.customer_name}")
        print(f"Movie Name      : {self.movie.movie_name}")
        print()
        print(f"Ticket Price    : ₹{self.movie.ticket_price}")
        print(f"Tickets Booked  : {self.number_of_tickets}")
        print("-" * 40)
        print(f"Total Amount    : ₹{total_amount}")
        print("=" * 50)


# Input
customer_name = input("Customer Name : ")
movie_name = input("Movie Name : ")
ticket_price = int(input("Ticket Price : "))
tickets = int(input("Tickets : "))

# Objects
customer = Customer(customer_name)
movie = Movie(movie_name, ticket_price)
booking = Booking(customer, movie, tickets)

booking.book_ticket()
booking.generate_receipt()