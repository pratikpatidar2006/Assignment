"""
1. Count Pairs with Difference K

A company records the ages of employees. Find how many pairs of employees have an age difference exactly equal to K.

Problem Statement:

Given an array of employee ages and an integer K, count the number of pairs whose absolute difference is K.

Example:

Input:

N = 5
K = 2
ages[] = {1, 5, 3, 4, 2}

Output:

3

Explanation:

(1,3), (3,5), (2,4)

"""

l=[]
n=int(input("Enter size of list :"))
k=int(input("Enter diffrence :"))

for i in range(n):
    x=int(input("Enter value :"))
    l.append(x)
print(l)

for i in range(n):
      for j in range(n):
             if l[j]-l[i]==k:
                  print(l[i],",",l[j])
            


