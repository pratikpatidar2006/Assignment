"""
6.

Product Code Verification System

An e-commerce company wants to verify whether two product codes are rearranged versions of each other.

Conditions:
- Ignore spaces
- Ignore case sensitivity

Input:
Enter first product code: Dormitory
Enter second product code: Dirty Room

Output:
Both Product Codes are Matching
"""
"""

n1=input("Enter first product code:")
n2=input("Enter second product code:")

if "".join(sorted(n1)).lower()=="".join(sorted(n2)).lower():
           print("Both Product Code are Matching")
             
else:
     print("Both Product Code aren't Matching")

"""
import math
n1=input("Enter first product code:").lower()
n2=input("Enter second product code:").lower()
i=0
if len(n1)!=len(n2):
       flag=False
else:
   flag=True
   for ch in n1:
     if n1.count(ch)!=n2.count(ch):
             flag=Flase
             break
if flag==True:
      print("Both Product Codes are Matching")
else:
      print("Both Product Codes are not Matching")


