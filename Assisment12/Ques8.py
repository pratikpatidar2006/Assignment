"""
8. Largest Smallest Sum Prime Checker

A number analyzer finds largest and smallest digit.

Write a program to:

- Find largest digit
- Find smallest digit
- Find sum of both
- Check whether sum is Prime or Not

Input:
57294

Output:
Largest = 9
Smallest = 2
Sum = 11
Prime
"""
import math
n=int(input("Enter number :"))
min=9
max=0
i=0
while n:
    mod=n%10
    if mod<min:          
         min=mod 
    if mod>max:          
         max=mod
    n=n//10
else:
    sum=min+max
    if sum<=1:
         print("Not a Prime Number")
    i=2
    while i<=math.sqrt(sum):
        if sum%i==0:
            print("Not a Prime Number")
            break
        i+=1
    else:
       print("Number is prime ")
         
print("largest number is",max)
print("Smallest number is",min)
print("Sum is :",min+max)
  
