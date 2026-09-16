"""
3.
Replace Consecutive Duplicate Characters with Single Character
Data Compression System

A cloud storage company wants to reduce unnecessary repeated characters in text logs.

Write a Python program that replaces consecutive duplicate characters with a single occurrence.

Input:
aaabbbccccdddaa
Output:
abcda
"""

n=input("Enter string:")
i=0
print(n[0],end="")
while i<len(n):
      if n[i]!=n[i-1]:
             print(n[i],end="")
      i+=1