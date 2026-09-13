"""
1.  Bank Customer Account Privacy System

A national bank is developing a secure customer portal where account
numbers should not be displayed completely on the screen. For security
reasons, the system should hide all digits except the last four digits
before showing them to users.

Conditions: - Display only the last 4 digits - Replace all previous
characters with *

Input: Enter account number: 123456789012

Output: Masked Account: ****9012
"""

# Manual Program

n=input("Enter account number:")
count=0
result=""
for i in n:
       count+=1
x=0
while x<count-4:
       result=result+"*"
       x+=1
else: 
       while x<count:
          result=result+n[x]
          x+=1
print(result)