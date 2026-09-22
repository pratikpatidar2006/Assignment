"""
# 2. AI Auto-Correct Consecutive Word Remover

An AI-powered typing assistant often captures duplicate consecutive words while converting speech into text.

The company wants a Python program that removes only consecutive duplicate words while preserving the original sentence structure.

### Input:

text
hello hello hello team meeting meeting started


### Output:

text
hello team meeting started

"""
n=input("enter string :")
n1=n.split(" ")
i=0
prev=""
while i<len(n1):
    if n1[i]!=prev:
      print(n1[i],end=" ")
      prev=n1[i]
    i+=1