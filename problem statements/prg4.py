class Guest:
    def __init__(self, name):
        self.name = name


class Room:
    def __init__(self, room_type, rate):
        self.room_type = room_type
        self.rate = rate


class Reservation:
    def __init__(self, guest, room, nights):
        self.guest = guest
        self.room = room
        self.nights = nights

    def total_amount(self):
        return self.room.rate * self.nights

    def invoice(self):
        print("=" * 50)
        print("              HOTEL INVOICE")
        print("=" * 50)
        print(f"\nGuest Name     : {self.guest.name}")
        print(f"Room Type      : {self.room.room_type}")
        print(f"\nNights Stayed  : {self.nights}")
        print(f"\nTotal Amount   : ₹{self.total_amount()}")
        print("\n" + "=" * 50)


guest_name = input("Guest Name: ")
room_type = input("Room Type: ")
nights = int(input("Nights Stayed: "))
rate = int(input("Room Rate: "))

guest = Guest(guest_name)
room = Room(room_type, rate)

reservation = Reservation(guest, room, nights)
reservation.invoice()