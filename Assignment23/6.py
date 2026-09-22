"""

# 6. AI Chat Toxic Pattern Detector

An AI moderation system wants to detect whether a sentence contains three consecutive repeating characters.

If found:

text
Spam Pattern Found


Else:

text
Clean Message


### Input:

text
heyyy broooo welcome


### Output:

text
Spam Pattern Found

"""

n=input("enter string :")
i=0
while i<len(n):
       if n[i]==n[i-1]==n[i-2] and i>=2:
              print("Spam pattern found")
              break
       i+=1 
else:
    print("Clean Message")
                