bal=0
while True:
   print("1. Deposit Money")
   print("2. Withdraw Money")
   print("3. Check Balance")
   print("4. Apply Interest")
   print("5. Exit")
   choice=int(input("Enter your choice: "))
   match choice:
       case 1:
          dep=int(input("Enter amount to deposite: "))
          bal=bal+dep
          print("Deposit Successful")
       case 2:
          w=int(input("Enter amount to withdrwal: "))
          if bal>=w:
             bal=bal-w
             print("Withdrawl Successful")
          else:
             print("insuficient fund")
       case 3:
          print("Currunt Balance: ",bal)
       case 4:
          if bal>50000:
             interest=(5/100)*bal
             updated=bal+interest
             print("Interest added: ",interest)
             print("Updated Balance: ",updated)
          else:
             interest=(3/100)*bal
             updated=bal+interest
             print("Interest added: ",interest)
             print("Updated Balance: ",updated)
       case 5:
           print("Exiting...")
           break 
       case __:
          print("plz enter correct choice: ")
          continue
        
           
         