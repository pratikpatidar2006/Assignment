balance=int(input("Enter your bank balance :"))

if balance<1000:
    print("Withdrawal not allowed")
elif balance<=5000:
    print("Maximum Withdrawal limit 1000")
else:
    print("Maximum Withdrawal Limit 5000")