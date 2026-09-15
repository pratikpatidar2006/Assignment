"""
6. Find Occurrence of a Word in a String

Product Review Analysis System

An e-commerce company wants to analyze customer reviews.

The company wants a Python program to count how many times a particular word appears in a review.

Input Sentence:


iphone is good and iphone battery is strong


Word:


iphone


Output:


2
"""
"""
n=input("Enter String:")
word=input("Enter word:")
count=0
n1=n.split(" ")
for ch in n1:
     if ch==word:
            count+=1
print(count)

"""
n=input("Enter String:")
word=input("Enter word:")
count=0
n1=""
for ch in n:
     if ch!=" ":
           n1=n1+ch
           if n1==word:
                   count+=1
                   
     else:
          if word==n1:
               count+=1
               n1=""
print(count)
             