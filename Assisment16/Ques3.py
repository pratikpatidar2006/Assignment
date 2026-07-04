"""WAP to find out all the leap years between two enterd years"""

a=int(input("enter first number: "))
b=int(input("enter second number: "))
i=a
while i<=b:
   if i%4==0:
      if i%100!=0 or i%400==0:
         print("leap year",i)
      else:
         print("Not a leap year",i)  
   else:
      print("Not a leap year",i)  
   i=i+1