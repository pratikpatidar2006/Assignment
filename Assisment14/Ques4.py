units=0
bill=0
while True:
   print("1. Enter Units Comsumed")
   print("2. Calculate Bill Amount")
   print("3. Apply Surcharge")
   print("4. Display Final Bill")
   print("5. Exit")
   choice=int(input("Enter the choice: "))
   match choice:
       case 1:
          u=int(input("Enter Unit Consumed: "))
          units=u
          print("Unit recorded successfully")
       case 2:
          if units<0:
             u=int(input("Please enter unit consumed first: "))
             units=u
             print("Unit recorded successfully")
          
          if units<=100:
             bill=units*5
          elif units<=200:
             bill=(100*5)+(units-100)*7
          else:
             bill=(100*5)+(units-100)*7+(units-200)*10
          print("Bill: ",bill)
       case 3:
          if bill>2000:
             splus=(10/100)*bill
             print("Surcharge: ",splus)
             bill=bill+splus
          else:
             splus=(5/100)*bill
             print("Surcharge: ",splus)
             bill=bill+splus
       case 4:
          print("Final Bill: ",bill)
       case 5:
          print("Exiting... Thank you!")
          break
 