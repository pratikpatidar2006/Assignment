"""
8.
AI Chat Moderation System

A social media company is developing an AI-based chat moderation system that analyzes user messages in real time.

During analysis, the system must identify special symmetric words (palindromes) because they are used as secret tags in internal testing.

A palindrome word is a word that reads the same forward and backward.

Write a Python program to find the first palindrome word present in the sentence.

If no palindrome word exists, print:

No palindrome word found
Input:
madam and arun went to level racecar station
Output:
madam

"""

n=input("enter string:")
word=""
rev=""
i=0
while i<=len(n):
      if i<len(n) and n[i]!=" " :
             word=word+n[i]
             
      else:
           rev=""
           j=0
           while j<len(word):
                 rev=word[j]+rev
                 j+=1
           if word==rev and word!="":
                   print("palindrome :",word)
          
           word=""
             
      i+=1
        
 
                