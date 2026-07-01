"""
7.
 Prime Sum Lucky Number

A lottery app checks if sum of digits is prime.

Write a program to:

- Find sum of digits
- If prime print Lucky Number
- Else Normal Number

Input:
4528

Output:
Sum = 19
Lucky Number

"""
import math
n=int(input("enter number:"))
sum=0
while n:
     mod=n%10
     sum=sum+mod
     n=n//10
else:
    print("Sum is ",sum)
    i=2
    if sum<=1:
         print("Normal Number")
    else:
         while i<=math.sqrt(sum):
            if sum%i==0:
                 print("Normal Number")
                 break
            i=i+1
         else:
             print("lucky prime number")
       
                 