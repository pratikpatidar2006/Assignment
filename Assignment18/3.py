"""

3.
Character Occurrence Checker in Product Review

An e-commerce website wants to know how many times a particular character appears in a product review.

Input: Enter product review: this product is really good Enter character to check: o

Output: Character 'o' occurs: 4 times

1).

n=input("Enter product review:")
count=0
for i in n:
    if i in 'o':
           count+=1
print(f"Character 'o' occurs: {count} times")

2).
"""
import math
n=input("Enter product review:")
count=0
i=1
while i<len(n):
        if 'o'==n[i]:
            count+=1
        i+=1
print(f"Character 'o' occurs: {count} times")