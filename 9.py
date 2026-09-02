"""
9.
Abundant Number Detector

A financial system analyzes surplus numbers.

An Abundant Number:
Sum of proper factors > number

Write a program to check Abundant Number.

Input:
12

Output:
Abundant Number

"""
n=int(input("Enter number :"))
fact=0
i=1
while i<=n//2:
      if n%i==0:
          fact=fact+i
      i+=1
print("fact is ",fact)
if fact>n:
    print("Abudant number ")
else:
    print("not a Abudant number ")