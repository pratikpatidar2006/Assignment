"""
7.
Adam Number Verification System – Question

A high-security digital system is designed to validate special mirrored numbers known as Adam Numbers before granting access to sensitive data.

When a user enters a numeric code, the system performs a dual verification process:

* It calculates the square of the entered number.
* It reverses the number and calculates the square of the reversed value.
* Finally, it checks whether both results are mirror images (reverses) of each other.

A number is called an Adam Number if:
The square of the number and the square of its reverse are reverses of each other.

Task:
Write a Python program to check whether a given number is an Adam Number or not.

Examples:

Input:
12
Output:
Adam Number

Input:
13
Output:
Not an Adam Number

Input:
11
Output:
Adam Number

Example:
12 → 12² = 144, reverse(12) = 21 → 21² = 441 → reverse of 144
"""
n=int(input("Enter number :"))
sqr=n**2
rev=0
while n:
      mod=n%10
      rev=rev*10+mod
      n=n//10
sqr2=rev**
2
rev2=0
while sqr2:
      mod=sqr2%10
      rev2=rev2*10+mod
      sqr2=sqr2//10

if rev2==sqr:
      print("Adam Number ")
else:
      print("Not Adam Number") 



