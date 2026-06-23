cart_value=int(input("Enter Cart Value"))
user_type=input("Enter user type (premium/regular)")

if cart_value>=5000:
     if user_type.lower()=="premium":
        cart_value=cart_value-cart_value*20/100
        print("Final amount:",cart_value)
     else:
        cart_value=cart_value-cart_value*10/100
        print("Final amount:",cart_value)
else:
    if cart_value>=2000:
        cart_value=cart_value-cart_value*5/100
        print("Final amount:",cart_value)
    else:
        print("Final amount:",cart_value)
        