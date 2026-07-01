"""
1. Product of Odd Numbers up to N

A puzzle game rewards players by multiplying odd numbers up to n.
Write a program using loops to find product of odd numbers.

Input:
5

Output:
15
"""

n=int(input("Enter Number: "))
p=1
for i in range(1,n+1):
   if i%2!=0:
      p=p*i
print(p)
