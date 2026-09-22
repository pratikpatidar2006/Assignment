
"""
3.
# Assignment: Prime Number Analyzer using List (Python)

## Scenario

A coaching institute stores student lucky numbers in a Python List.
Your task is to analyze the list and identify prime numbers for a scholarship selection process.

You must iterate through every element of the list and perform prime number analysis.

---
"""
n=int(input("enter length of array "))
list=[]
sum=0
for i in range(n):
      x=input("enter your lucky number : ")
      list.append(x)
for i in list[:]:
      i=int(i)
      count=0
      for v in range(2,i):
          if i%v==0:
              count+=1
      if count==0:
              print(i)

              