import math
while True:
   print("1. Check Prime Number")
   print("2. Palindrome Number")
   print("3. Reverse a Number")
   print("4. Count Digit")
   print("5. Exit")
   choice=int(input("Enter your choice: "))
   match choice:
       case 1:
          n=int(input("Enter a Number: "))
          if n<=1:
             print(n," is Not a Prime Number")
          else:
             i=2
             for i in range(i,int(math.sqrt(n))):
                if n%i==0:
                   print(n," is Not a Prime Number")
                   break
             else:
                print(n," is a Prime Number")
          again=input("Do you want to Continue(yes/no): ")
          match again:
               case "yes":
                  continue
               case "no":
                  print("Thanq")
                  break
               case __:
                  print("Wrong input")           
       case 2:
          n=int(input("Enter a Number: "))
          r=0
          t=n
          while n:
             r=r*10+n%10
             n=n//10
          if t==r:
             print(n," is Palindrome")
          else:
             print(n," is Not Palindrome")
          again=input("Do you want to Continue(yes/no): ")
          match again:
               case "yes":
                  continue
               case "no":
                  print("Thanq")
                  break
               case __:
                  print("Wrong input") 
       case 3:
          n=int(input("Enter Number: "))
          rev=0
          while n:
             rev=rev*10+n%10
             n=n//10
          print("Reversed Number is: ",rev)
          again=input("Do you want to Continue(yes/no): ")
          match again:
               case "yes":
                  continue
               case "no":
                  print("Thanq")
                  break
               case __:
                  print("Wrong input") 
       case 4:
           n=int(input("Enter Number: "))
           count=0
           while n:
              count+=1
              n=n//10
           print("Total digit: ",count)
           again=input("Do you want to Continue(yes/no): ")
           match again:
               case "yes":
                  continue
               case "no":
                  print("Thanq")
                  break
               case __:
                  print("Wrong input") 
       case 5:
          print("Exiting... Thank you!")
          break 
       case __6:
          print("Please enter correct choice:")
          continue
       
         