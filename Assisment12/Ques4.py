"""
4. Prime Security Code Checker – Advanced

A high-security lab accepts only prime numbered access codes.

When a user enters a number, the software must:

- Check whether number is prime
- If prime, print next immediate prime number
- If not prime, print previous immediate prime number

Write a program using loops only.

Input:
29

Output:
Prime Number
Next Prime = 31
"""

import math
prime=False
n=int(input("Enter number"))
if n<=1:
    print("Not a Prime Number")
    print("No previous ")
    
else:
   i=2
   while i<=math.sqrt(n):
      if n%i==0: 
         print("Number is not Prime")  
         break
      i+=1
   else:
       print("Number is Prime") 
       prime=True
if prime:
       while True:
           n+=1
           if n<=1:
               print("Not a Prime Number")
           else:
               i=2
               while i<=math.sqrt(n):
                  if n%i==0: 
                    
                     break
                  i+=1
               else:
                   print("Next Prime Number is ",n) 
                   break
elif n>1:
      while True:
            n-=1
            if n<=1:
                print("Not a Prime Number")
            else:
                i=2
                while i<=math.sqrt(n):
                    if n%i==0:
                        break
                    i+=1
                else:
                    print("Previous Prime Number is ",n)
                    break
                    
                    
    
      
         
             
             
   