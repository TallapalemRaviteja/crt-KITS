class Subscription:
    def features(self):
        print("Watch videos with advertisements")

class PremiumSubscription(Subscription):
    def features(self):
        print("Watch videos without advertisements")
user_input = input().strip()
if user_input == "Premium Plan":
    plan = PremiumSubscription()
    plan.features()
elif user_input == "Basic Plan":
    plan = Subscription()
    plan.features()