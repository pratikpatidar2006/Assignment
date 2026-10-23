"""
2.
Secure Password Analysis

A cybersecurity team wants to identify pairs of passwords having no common characters.

Problem Statement:

Given N strings, count the number of pairs that do not share any common character.

Example:

Input

N = 4
passwords[] = {"abc", "de", "fg", "ad"}

Output

3

Explanation

("abc","de")
("abc","fg")
("de","fg")

"""
l=[]
n=int(input("Enter size of list :"))
for i in range(n):
   res=True
   k=l[i]
   while True:
      for j in range(i+1,n):
        for x in range(len(k)):
           if k[x] not in l[i+1]:
                  pass
           else:
                res=False
                break
      print(l[i])   
       
                 