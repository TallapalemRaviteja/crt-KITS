class Passenger:
    def __init__(self, name):
        self.name = name


class Flight:
    def __init__(self, flight_no):
        self.flight_no = flight_no


class BoardingPass:
    def __init__(self, passenger, flight, seat):
        self.passenger = passenger
        self.flight = flight
        self.seat = seat

    def display(self):
        print("=" * 50)
        print("               BOARDING PASS")
        print("=" * 50)
        print(f"\nPassenger Name : {self.passenger.name}")
        print(f"Flight Number  : {self.flight.flight_no}")
        print(f"Seat Number    : {self.seat}")
        print("\nStatus         : CHECK-IN COMPLETE\n")
        print("=" * 50)


class Airport:
    occupied_seats = set()

    def assign_seat(self, seat):
        if seat not in Airport.occupied_seats:
            Airport.occupied_seats.add(seat)
            return seat
        return None


name = input("Passenger Name: ")
flight_no = input("Flight Number: ")
seat = input("Seat Number: ")

passenger = Passenger(name)
flight = Flight(flight_no)

airport = Airport()
assigned = airport.assign_seat(seat)

if assigned:
    bp = BoardingPass(passenger, flight, assigned)
    bp.display()
else:
    print("Seat already occupied.")