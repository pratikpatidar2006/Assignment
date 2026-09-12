"""
2.
Mobile Number Digit Counter

A telecom company wants to count how many digits are present in a customer contact number entered with spaces or symbols.

Input:
Enter contact number: +91 98765-43210

Output:
Total digits: 12
"""

import math
n=input("Enter contact number:")
count=0
for i in n: 
     if i<="9" and i>="0":
        count+=1
print("Total digits:",count)