"""
5. Find the Number of Unique Characters in a String

Password Strength Analyzer

A cybersecurity company checks password strength based on the number of unique characters present.

Passwords containing more unique characters are considered more secure.

Write a Python program to count the number of unique characters in a string.

Input:


aabbccdde


Output:


5
"""

n=input("Enter String:")
visited=""
count=0
for ch in n:
     if ch not in visited:
             count+=1
             visited=visited+ch
print("Total no of unique character :",count)
     