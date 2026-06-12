class Customer:
    def __init__(self, name, mobile):
        self.name = name
        self.mobile = mobile


class RechargePlan:
    def __init__(self, plan_name, amount):
        self.plan_name = plan_name
        self.amount = amount


class Recharge:
    def __init__(self, customer, plan):
        self.customer = customer
        self.plan = plan

    def generate_receipt(self):
        print("=" * 50)
        print("             RECHARGE RECEIPT")
        print("=" * 50)
        print(f"\nCustomer Name : {self.customer.name}")
        print(f"\nPlan Selected : {self.plan.plan_name}")
        print(f"\nAmount Paid   : ₹{self.plan.amount}")
        print("\nStatus        : SUCCESSFUL\n")
        print("=" * 50)


name = input("Customer Name: ")
mobile = input("Mobile Number: ")
plan_name = input("Plan Name: ")
amount = int(input("Amount: "))

customer = Customer(name, mobile)
plan = RechargePlan(plan_name, amount)

recharge = Recharge(customer, plan)
recharge.generate_receipt()