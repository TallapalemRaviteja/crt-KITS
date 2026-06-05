def addition(a,b):
  print(f"Addition of {a} and{b} is {a+b}")
def subtraction(a,b):
  print(f"Subtraction of {a} and {b is {a-b}}")
def multliply(a,b):
  print(f"Multiplication of {a} and {b} is {a*b}")
def division(a,b):
  print(f"Division of {a} and {b} is is {a/b}")
def remainder(a,b):
  print("remainder of {a} and {b} is {a%b} ")  
while True:
  print("1. addtion")
  print("2. subtraction")
  print("3. multiplication")
  print("4. division")
  print("5. remainder")
  print("6. Exit")
  print("--------------------------------")
  choice = int(input("Enter choice"))
  if choice == 0:
    break
  a = int(input("Enter first number: "))
  b = int(input("Enter second number: "))
  if choice  == 1:
    addition(a,b)
  elif choice == 2:
    subtraction (a,b)
  elif choice == 3: 
    multliply(a,b)
  elif choice == 4:
    division(a,b)  
  elif choice == 5:
    remainder(a,b)
  print("\n")