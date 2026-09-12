"""
Test Case 2:
Input:
Enter citizen information:
DEEPIKA pADukone ward number 12

Output:
Formatted Information:
DEEPIKA PADukone Ward Number 12


Test Case 3:
Input:
Enter citizen information:
government engineering college bhopal zone 3

Output:
Formatted Information:
Government Engineering College Bhopal Zone 3


Test Case 4:
Input:
Enter citizen information:
python FULL stack developer batch 18

Output:
Formatted Information:
Python FULL Stack Developer Batch 18
"""
import math
n=input("enter number")
i=0
result=""
if n[0]<="z" and n[0]>="a":
     result=result+chr(ord(n[i])-32)
i=1
while i<len(n):
      if n[i]!=" " and n[i-1]==" ":
            if n[i]<="z" and n[i]>="a":
                result=result+chr(ord(n[i])-32)
            else:
                result=result+n[i]
     
      else:
        result=result+n[i]
      i+=1

print(result)