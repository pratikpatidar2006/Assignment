"""

4. Program should work for both uppercase and lowercase letters.

 Find the Shortest Word in a Sentence

Telecom SMS Cost Optimization System

A telecom company charges customers based on the length of words used in bulk SMS campaigns.

The company wants to identify the shortest word in every message for analytics purposes.

Write a Python program to find the shortest word from a given sentence.

Input:


Python is very easy to learn


Output:


is
"""
n=input("Enter message:")
word=""
small=""
count1=len(n)
count=0
i=0
while i<len(n):
      if n[i]!=" ":
           count=count+1
           word=word+n[i]
      else:
         if count1>count:
                count1=count
                small=word
                count=0
                word=""
      i+=1
print(small)