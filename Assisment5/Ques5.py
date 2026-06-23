username=input("Enter username")
password=input("Enter password")

if username=="admin":
    print("valid user")
    if len(password)>=8:
       print("Strong Password")
else:
    print("Invalid User")