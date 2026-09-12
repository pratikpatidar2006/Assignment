"""
1.
Email Username Validator

A company wants to check whether an employee email username is valid before creating an official account.

Conditions:
- Username should start with a letter
- Username can contain letters, digits, underscore (_)
- No spaces allowed
- Length should be between 5 and 12 characters

Input:
Enter username: ajay_123

Output:
Valid Username

"""
import math
n=input("enter username :")
i=0
check=0
check1=0
if (n[0]<="Z" and n[0]>="A") or (n[0]<="z" and n[0]>="a"):
      check=1
if check==1:
   while i<len(n):
       if (n[i]<="9" and n[i]>="0") or (n[i]<="z" and n[i]>='a') or (n[i]<="Z" and n[i]>='A') or (n[i]=="_"):
                check1=1
       else:
                check1=0
                break
       i+=1
            
if check==1 and check1==1 and len(n)<=12 and len(n)>=5:
         print("Valid Username")
else:
        print("Not Valid Username ")