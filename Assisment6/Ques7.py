experience,rating,salary=map(int,input("Enter values :").split())
 
if experience>=5:
     if rating>=4:
         if salary<50000:
              bonus=salary*20/100
              print("Bonus:",bonus)
         else:
              bonus=salary*10/100
              print("Bonus:",bonus)
     else: 
              bonus=salary*5/100
              print("Bonus:",bonus)
else:
     print("No Bonus is Given")