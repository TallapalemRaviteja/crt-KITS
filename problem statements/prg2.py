class Vehicle:
    def __init__(self, vehicle_no):
        self.vehicle_no = vehicle_no


class ParkingManager:
    def __init__(self, rate):
        self.rate = rate

    def calculate_fee(self, hours):
        return hours * self.rate

    def generate_receipt(self, vehicle, hours):
        fee = self.calculate_fee(hours)

        print("=" * 50)
        print("              PARKING RECEIPT")
        print("=" * 50)
        print(f"\nVehicle Number : {vehicle.vehicle_no}")
        print(f"Hours Parked   : {hours}")
        print(f"\nParking Fee    : ₹{fee}\n")
        print("=" * 50)


vehicle_no = input("Vehicle Number: ")
hours = int(input("Hours Parked: "))
rate = int(input("Rate Per Hour: "))

vehicle = Vehicle(vehicle_no)
manager = ParkingManager(rate)

manager.generate_receipt(vehicle, hours)