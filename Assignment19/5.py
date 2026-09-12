"""
Palindrome Product Code Checker

A factory wants to identify whether a product code reads the same forward and backward.

Input:
Enter product code: MADAM

Output:
Palindrome Code

Input:
Enter product code: PRODUCT

Output:
Not a Palindrome Code

1)with function
"""
n=input("enter product code:")
if n[::-1]==n:
      print("palindrome code")
else:
      print("not a palindrome code")


# without function

n=input("enter product code:")
rev=""
for i in n:
    rev=i+rev
if rev==n:
      print("palindrome code")
else:
      print("not a palindrome code")

# method 3
import math
n=input("enter product code:")
i=0
flag=True
for i in range(len(n)//2):
      if n[i]!=n[len(n)-i-1]:
             flag=False
if flag==True:
     print("palindrome Code")
else:
     print("Not Palindrome")
    

