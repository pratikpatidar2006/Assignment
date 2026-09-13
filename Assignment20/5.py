"""
5. Website URL Verification System

A software company is developing an automated website registration
portal. Before saving a website address, the system must verify whether
the URL follows the required company format.

Conditions: - Must start with www - Must end with .com

Input: Enter website: www.amazon.com

Output: Valid Website
"""

n=input("Enter website:")
flag=False
flag1=False
if "www"==n[:3]:
       flag=True
if ".com"==n[-4:]:
        flag1=True
if flag==True or flag1==True:
         print("Valid website")
else:
       print("Invalid Website")
       