class Owner:
    def __init__(self, owner_name):
        self.owner_name = owner_name


class Pet:
    def __init__(self, pet_name):
        self.pet_name = pet_name


class Appointment:
    appointments = []

    def __init__(self, owner, pet, service, charge):
        self.owner = owner
        self.pet = pet
        self.service = service
        self.charge = charge
        Appointment.appointments.append(self)

    def generate_receipt(self):
        print("=" * 50)
        print("            SERVICE RECEIPT")
        print("=" * 50)
        print(f"\nOwner Name : {self.owner.owner_name}")
        print(f"Pet Name   : {self.pet.pet_name}")
        print(f"\nService    : {self.service}")
        print(f"\nAmount     : ₹{self.charge}")
        print("\n" + "=" * 50)


owner_name = input("Owner Name: ")
pet_name = input("Pet Name: ")
service = input("Service: ")
charge = int(input("Charge: "))

owner = Owner(owner_name)
pet = Pet(pet_name)

appointment = Appointment(owner, pet, service, charge)
appointment.generate_receipt()