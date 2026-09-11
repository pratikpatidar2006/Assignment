"""
2.
Space Counter in Chat Messages

A chat application wants to calculate how many spaces are used in a message.

Input: Enter chat message: Good morning everyone how are you

Output: Total spaces: 5
"""
ch=input("Enter chat message:")
count=0
for i in ch:
      if i in " ":
         count+=1
print(count)