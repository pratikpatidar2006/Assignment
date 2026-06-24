stock=int(input("Enter stock :"))
priority=input("Enter priority :")
if stock>=100:
     if priority=="high":
         distance=int(input("Enter Distance :"))
         if distance<=200:
             print("Dispatch Immediately")
         else:
             print("Use Fast Courier")
     else:
          if stock>=300:  
             print("Bulk Dispatch")
          else:
             print("Normal Dispatch")
elif stock<50:
        print("mark out of stock")
     
else:
     if stock>=50:
          print("priority is High , partially dispatch")
     else:
          print("Hold")
          
      
        
      
