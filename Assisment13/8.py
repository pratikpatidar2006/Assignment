""" 
8.

 ATM Note Counter


A bank ATM dispenses ₹100 notes.


Write a program to:


- Read withdrawal amount

- Count how many ₹100 notes needed using loop


Input:

700


Output:

Notes = 7

"""
n=int(input("Enter Amount:"))
count=0
while n>100:
      count+=1
      n=n-100
print("Total count of 100 notes needed :",count)

