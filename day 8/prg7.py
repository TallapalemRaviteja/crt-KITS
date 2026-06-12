role = input()

class Employee:
    def bonus(self):
        print("Bonus: 5000")

class Manager(Employee):
    def bonus(self):
        print("Bonus: 20000")

if role == "Manager":
    obj = Manager()
else:
    obj = Employee()

obj.bonus()