attendence=int(input("Enter Attendence Percentage :"))
if attendence>=75:
    print("Eligible")
elif attendence>=60:
    print("Eligible with warning")
else:
    print("Not Eligible")
