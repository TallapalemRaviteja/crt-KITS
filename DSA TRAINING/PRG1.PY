pin=input("Enter the password :")
try:
    if pin=="1234":
        print("Login successful")
    else:
        raise TypeError("Incorrect password")
except TypeError as e:
    print(e)    