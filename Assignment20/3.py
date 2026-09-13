"""
3.  Smart Chat Message Cleaner

A social media company noticed that users often enter messages with
unnecessary spaces. To improve readability and storage efficiency, the
system should remove extra spaces and keep only a single space between
words.

Input: Enter message: Java is easy

Output: Cleaned Message: Java is easy
"""

n=input("Enter message :")
result=""
count=0

for x in n:
     count+=1
i=0
while i<count:
     if n[i]==" " and n[i+1]==" ":
            pass
     else:
          result=result+n[i]
     i+=1
print("Cleaned message :",result)
           
     