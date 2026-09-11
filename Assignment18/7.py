"""
.
Vehicle Number Plate Checker

The traffic department wants to validate vehicle registration numbers.

Conditions:
- First 2 characters should be alphabets
- Next 2 should be digits
- Total length should be 10

Input:
Enter vehicle number: MP04AB1234

Output:
Valid Vehicle Number
"""
import math
n=input("Enter vehicle Number:").upper()
i=0
check=0

if n[0]<="Z" and n[0]>="A"  and n[1]>="A"  and n[1]<="Z" and n[2]<="9" and n[2]>="0" and  n[3]<="9" and n[3]>="0":
              check=1
if len(n)==10 and check==1 :
        print("Valid Vehicle Number")
else:
        print("Not a valid Number ")