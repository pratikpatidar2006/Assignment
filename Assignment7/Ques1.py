unit=int(input("Enter Unit :"))
if unit<=100:
     bill=5*unit   
elif unit<=200:
     bill=5*100+7*(unit-100) 
else:
     bill=5*100+7*100.3+10*(unit-200)
print("Total Bill is",bill)