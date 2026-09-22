"""
3. Secure Banking Transaction Analyzer

A banking server generates encrypted transaction IDs using letters and digits.

The fraud detection team wants a Python program to find the first digit that does not repeat in the transaction ID.

If no unique digit exists, print:

text
No unique digit found


### Input:

text
A122334455667789


### Output:

text
8
"""

n=input('enter string:')
for ch in n:
      if ch<="9" and ch>="0":
             count=n.count(ch)
             if count==1:
                  print(ch)
                  break
if count!=1: 
         print("no unique digit found")
           