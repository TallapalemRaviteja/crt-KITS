size = input("Enter pizza size (small/medium/large): ")

if size == "small":
    bill = 10
elif size == "medium":
    bill = 15
elif size == "large":
    bill = 20

n = int(input("Enter number of toppings: "))

for i in range(n):
    topping = input("Enter topping: ")

    if topping == "cheese":
        bill = bill + 2
    elif topping == "pepperoni":
        bill = bill + 3
    elif topping == "olives":
        bill = bill + 5
    elif topping == "jalapenos":
        bill = bill + 5

print("Total Bill = $", bill)