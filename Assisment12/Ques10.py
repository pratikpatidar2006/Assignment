"""
Zero Count Prime Scanner

A banking system checks account numbers.

Write a program to:

- Count zero digits
- Find sum of digits
- Add zero count and sum
- Multiply by smallest digit
- Check whether final result is Prime or Not

Input:
908406

Output:
Zero Count = 2
Sum = 27
Smallest Digit = 0
Final Result = 0
Not Prime

"""
import math
n=int(input("Enter Number :"))
count0=0
sum=0
small=9
while n:
     mod=n%10
     sum=sum+mod
     if mod==0:
         count0+=1
     if mod<small:
         small=mod
     n=n//10
print("Zero Count ",count0)
print("Sum is",sum)
print("Smallest Digit ",small)
final=(count0+sum)*small
if final<=1:
      print("Not a Prime Number ")
else:
     i=2
     while i<=math.sqrt(final):
         if final%i==0:
             print("Not A Prime Number")
             break
         i+=1
     else:
          print("Prime Number")
