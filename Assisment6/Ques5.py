acc_bal=int(input("Enter account Balance : "))
wdw_amt=int(input("Enter withdraw Balance : "))
pin_status=input("Correct/Incorrect")

if acc_bal>=wdw_amt:
     if wdw_amt<=10000:
         if pin_status.lower()=="correct":
             print("Transaction succesful")
         else:
             print("Invalid PIN ")
     else:
         print("Limit Exceeded")
else:
   print("Insufficient Fund")