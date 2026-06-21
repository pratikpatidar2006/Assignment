mobile_price=int(input("Mobile price="))
down_pay=int(input("Down payment ="))
interest_rate=int(input("Interest rate ="))
months=int(input("Months ="))
remaining=(mobile_price)-(down_pay)
interest=remaining*(interest_rate/100)
print("Remaining Amount :",remaining)
print("Total with Interest :",remaining+interest)
monthly_emi=remaining/months
print("Monthly EMI :",monthly_emi)



