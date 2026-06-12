class Member:
    def __init__(self, name):
        self.name = name


class MembershipPlan:
    def __init__(self, plan_name, monthly_fee):
        self.plan_name = plan_name
        self.monthly_fee = monthly_fee


class Gym:
    def generate_receipt(self, member, plan, duration):
        total_fee = plan.monthly_fee * duration

        print("=" * 50)
        print("             MEMBERSHIP RECEIPT")
        print("=" * 50)
        print(f"\nMember Name : {member.name}")
        print(f"\nPlan        : {plan.plan_name}")
        print(f"\nDuration    : {duration} Months")
        print(f"\nTotal Fee   : ₹{total_fee}")
        print("\n" + "=" * 50)


member_name = input("Member Name: ")
plan_name = input("Plan Name: ")
duration = int(input("Duration (Months): "))
monthly_fee = int(input("Monthly Fee: "))

member = Member(member_name)
plan = MembershipPlan(plan_name, monthly_fee)

gym = Gym()
gym.generate_receipt(member, plan, duration)