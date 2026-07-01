"""
9.Even Odd Difference Prime System

A smart scanner counts even and odd digits.

Write a program to:

- Count even digits
- Count odd digits
- Find difference
- Check whether difference is Prime or Not

Input:
123456

Output:
Even Count = 3
Odd Count = 3
Difference = 0
Not Prime
"""

import math
n=int(input("Enter Number:"))
counte=0
counto=0

while n:
      mod=n%10
      if mod%2==0:
          counte+=1
      else:
          counto+=1
      n=n//10
diff=abs(counte-counto)
if diff<=1:
   print("Not a Prime Number")
else:
   i=2
   while i<=math.sqrt(diff):
      
     if diff%i==0:
         print("Not Prime")
         break
     i=i+1
   else:
    print("Prime Number ",diff)
         
        
      
   