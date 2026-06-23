unit=int(input("Enter number of unit : "))

if unit>=100:
    if unit>=300:
       print("High Usage")
    else:
       if unit>=200:
          print("Moderate Usage")
       else:
          print("Normal Usage")
else:
   print("Low Usage")

       