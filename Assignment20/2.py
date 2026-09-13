"""

2.  Corporate Employee Short ID Generator

A multinational company wants to automatically generate short IDs for
employees while creating official email accounts. The system should take
the employee’s full name and create an ID using the first character of
each word.

Conditions: - Take first character of every word - Convert all
characters to uppercase

Input: Enter employee name: ajay singh thakur

Output: Employee Short ID: AST
"""
result=""
n=input('Enter employee name:')
i=0
if n[0]>="a" and n[0]<="z":
           result=result+chr(ord(n[0])-32)
           i+=1
else:
      result=result+n[0]
      i+=1
while i<len(n):
       if n[i-1]==" " and n[i]<="z" and n[i]>="a":
            result=result+chr(ord(n[i])-32)
       else:
            if n[i-1]==" ":
                  result=result+n[i]
       
       i+=1
print("Employee short Id :",result)
           
                 
      