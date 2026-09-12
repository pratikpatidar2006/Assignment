"""
4.
Employee ID Validator

A company wants to validate employee IDs before storing them in the database.

Conditions:
- ID must start with "EMP"
- Total length should be 8
- Remaining characters should be digits only

Input:
Enter Employee ID: EMP10234

Output:
Valid Employee ID
"""
import math
n=input("Enter Employee ID:")
i=0
if len(n)==8 and n[:3]=="PNR" and n[3:].isdigit():
            print("Valid Employee ID")
else:
           print("Invalid Employee ID")