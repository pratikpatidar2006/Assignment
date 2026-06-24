exp=int(input("How many years of Experience :"))
salary=int(input("Enter your Salary :"))
if exp>10:
     bonus=salary*20/100
     print("Bonus Amount :",bonus)
elif exp>5:
     bonus=salary*10/100
     print("Bonus Amount :",bonus)
elif exp>10:
     bonus=salary*5/100
     print("Bonus Amount :",bonus)
else:
     print("No Bonus")