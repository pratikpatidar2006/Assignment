"""
4. Strong Number Checker

A digital lock opens only for strong numbers.

A strong number is a number whose sum of factorial of digits equals the number.

Example:
145 = 1! + 4! + 5!

Write a program using loops to check strong number.

Input:
145

Output:
Strong Number
"""

n=int(input("enter number: "))
sum=0
temp=n
while n:
   d=n%10
   fact=1
   for i in range(1,d+1):
      fact=fact*i
   sum=sum+fact
   n=n//10
if temp==sum:
   print("Strong Number")
else: 
   print("Not a Strong Number")
