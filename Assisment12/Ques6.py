"""
Composite Number Detector – Risk Version

A product company marks composite numbers as risky.

User enters a number.
System must:

- Check Composite or Not
- Count total factors
- Print smallest factor other than 1

Input:
12

Output:
Composite Number
Factors Count = 6
Smallest Factor = 2
"""

n=int(input("enter number: "))
count=0
small=n//2   
if n<=1:
   print("Not Composite")
   print("Factor count :",n)
   print("Smallest Factor :",n)

   
else:  
   i=2     
   while i<=n//2:  
      if n%i==0:
         count+=1
         if i<=small:
            small=i
      i=i+1
if count>=2:
   print("Composite Number")
   print("Factor Count",count+2)
   print("small facotor",small)

      
      

