sal=0
net=0
while True:
   print("1. Enter Basic Salary: ")
   print("2. Calculate HRA(20%) and DA(10%)")
   print("3. Calculate Net Salary")
   print("4. Tax Deduction")
   print("5. Display Salary Slip")
   print("6. Exit")
   choice=int(input("Enter your choice: "))
   match choice:
      case 1:
         sal=int(input("Enter Basic Salary: "))
         print("Salary enterd successfully")
      case 2:
         if sal<0:
           sal=int(input("Please enter basic salary first: ")) 
         hra=(20/100)*sal
         da=(10/100)*sal
         print("HRA: ",hra)
         print("DA: ",da)
      case 3:
         if sal<0:
           sal=int(input("Please enter basic salary first: "))
         hra=(20/100)*sal
         da=(10/100)*sal
         net=sal+hra+da
         print("Net Salary(before tax): ",net)
      case 4:
         if sal>50000:
            sal=sal-(10/100)*sal
            print("Salary After Taxation: ",sal)
         else:
            sal=sal-(5/100)*sal
            print("Salary After Taxation: ",sal)
      case 5:
         print("Salary Slip:-")
         print("Basic Salary - ",sal)
         print("HRA - ",hra)
         print("DA - ",da)
         print("Net Salary - ",net)
         print("Salary after Taxation - ",sal)
      case 6:
         print("Exiting... Thank you!")
         break
      case __:
         print("Plz enter correct choice: ")
         continue