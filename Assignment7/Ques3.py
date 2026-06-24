income=int(input("Enter Annual Income:"))
if income<=250000:
      print("No Tax")
elif income<=500000:
      print(income*5/100)
elif income<=1000001:
      print(income*20/100)
else:
      print(income*30/100)