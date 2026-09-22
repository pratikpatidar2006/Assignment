"""
# 7. Enterprise Password Pattern Strength Analyzer

A cybersecurity company wants to validate advanced passwords.

## Conditions:

* Minimum 10 characters
* At least:

  * 1 uppercase letter
  * 1 lowercase letter
  * 1 digit
  * 1 special character
* No consecutive repeating characters
* No spaces allowed

### Input:

text
Pyth@n1234


### Output:

text
Strong Password


### Input:

text
Paaass@12


### Output:

text
Weak Password


---
"""
upper=0
lower=0

digit=0
special=0
n=input("##### Input :")
if len(n)>=10:
   for ch in n:
     if ch!=" ":
       if ch<="Z" and ch>="A":
              upper+=1
       elif ch<="z" and ch>="a":
              lower+=1
       elif ch<="9" and ch>="0" :
             digit+=1
       else:
             special+=1
    
if upper>=1 and lower>=1 and digit>=1 and special>=1:
     
        print("Strong password")
else:
           print("Weak password")