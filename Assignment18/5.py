"""
5.
Advanced Password Security Checker

A cyber security company wants to verify whether employee passwords are highly secure before giving system access.

Conditions: Password must:

Start with an uppercase letter
End with a digit
Contain at least 2 digits
Contain at least 1 special character (@ # $ % & *)
Must not contain spaces
Length should be between 8 and 15 characters

Input: Enter password: Python@45

Output: Secure Password

"""

import math
n=input("Enter password:")
upper=end=digit=special=space=0

if n[0]<="Z" and n[0]>="A":
        upper=1
        if n[-1]<="9" and n[-1]>="0":
              end=1
i=0
if len(n)<=15 and len(n)>=8:
    while i<len(n):
        if n[i]<="9" and n[i]>="0":
               digit+=1
        if n[i]==" ":
               space=1
        if n[i] in "@#$%&*":
                special=1
        i+=1

if digit+end>=2 and upper==1 and space==0 and end==1 and special==1 :
              print("Secure password")
else:
              print("Insecure Password")
  
       
            