"""

4.  Instant Messaging Word Encryption System

A messaging application wants to temporarily encrypt messages during
transmission. The encryption rule is to reverse every word individually
while keeping the word positions unchanged.

Input: Enter message: java is powerful

Output: Encrypted Message: avaj si lufrewop
"""

n=input("Enter message:")
i=0
rev=""
while i<len(n):
      if n[i]!=" ":
            rev=n[i]+rev
      else:
            rev=rev+n[i]
            print(rev,end="")
            rev=""
      i+=1
print(rev)
            